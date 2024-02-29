from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View,DetailView,ListView
from accounts.models import Movie,Favourite
from django.forms import modelformset_factory
from .forms import MovieForm,CrewForm,UserUpdateForm
from accounts.models import MovieCast
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

# Create your views here.


class IndexView(View):
    def get(self,request):
        mov=Movie.objects.all()
        for m in mov:
            types=m.type
        context={'movies':mov,
                 'type':types
                 }
        return render(request,'index.html',context)
    

class MovieDetailView(DetailView):

    template_name="detail.html"
    pk_url_kwarg='id'
    queryset=Movie.objects.all()
    context_object_name='movie'


class PlayVideoView(View):

    def get(self,request,*args,**kwargs):
        m_id=kwargs.get('id')
        movie=Movie.objects.get(id=m_id)
        return render(request,'playvideo.html',{'movie':movie})


class ProfileView(View):
    def get(self,request):
        movie=Movie.objects.filter(user=self.request.user)
        return render(request,"profile.html",{'movies':movie})

    

class UploadListView(ListView):

    template_name= "profile.html"
    context_object_name='movie'
    # queryset=Movie.objects.all()

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user)


    


class UploadMovieView(View):
    
    def get(self, request):
        CrewFormSet = modelformset_factory(MovieCast, form=CrewForm, extra=0)
        form = MovieForm()
        formset = CrewFormSet(queryset=MovieCast.objects.none())
        return render(request, 'upload.html', {'form': form, 'formset': formset})
    
    def post(self, request):

        MovieFormSet = modelformset_factory(MovieCast, form=CrewForm, extra=0)
        form = MovieForm(request.POST, request.FILES)
        formset = MovieFormSet(request.POST, queryset=MovieCast.objects.none())
        if form.is_valid() and formset.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            form.save_m2m()

            for crew_form in formset:
                if crew_form.cleaned_data:
                    crew = crew_form.save(commit=False)
                    crew.save()
                    movie.crew.add(crew)
            return redirect('profile')
        return render(request, 'upload.html', {'form': form, 'formset': formset})
    
class ProfileEditView(View):

    def get(self,request,*args,**kwargs):
        u_id=kwargs.get('id')
        user_obj=User.objects.get(id=u_id)
        form=UserUpdateForm(initial={'first_name':user_obj.first_name,'last_name':user_obj.last_name,'email':user_obj.email,'username':user_obj.username})
        return render(request,'update_profile.html',{'form':form})

    def post(self,request,*args,**kwargs):
        u_id=kwargs.get("id")
        user_obj=User.objects.get(id=u_id)
        form_data=UserUpdateForm(data=request.POST)
        if form_data.is_valid():
            user_obj.first_name=form_data.cleaned_data.get('first_name')
            user_obj.last_name=form_data.cleaned_data.get('last_name')
            user_obj.email=form_data.cleaned_data.get('email')
            user_obj.username=form_data.cleaned_data.get('username')
            user_obj.save()
            return redirect('profile')
        else:
            return redirect(request,'update_profile.html',{'form':form_data})


class SearchView(View):

     def post(self, request):

        result = request.POST.get('search')
        print("Search term:", result)
        ser = Movie.objects.filter(Q(name__icontains=result) | Q(type__icontains=result))
        if ser:
            print("Query results:", ser)
            return render(request, 'search.html', {'result': ser})
        else:
            messages.error(request,'Not Found')
            return render(request,'search.html')
        
class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):
        mid=kwargs.get('id')
        mov_obj=Movie.objects.get(id=mid)
        form=MovieForm(instance=mov_obj)
        return render(request,'editmovie.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        mid=kwargs.get('id')
        mov_obj=Movie.objects.get(id=mid)
        form_data=MovieForm(data=request.POST,instance=mov_obj,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('profile')
        else:
            return render(request,'editmovie.html',{'form':form_data})
        

class MovieDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        mid=kwargs.get('id')
        Movie.objects.get(id=mid).delete()
        return redirect('profile')
    

class CategoryView(View):

    def get(self,request,*args,**kwargs):
        genre=kwargs.get('cat')
        movies=Movie.objects.filter(type=genre)
        print(movies)
        context={
            'movie':movies,
            'genre':genre
        }
        return render(request,'category.html',context)
    
class AddToFavouriteView(View):

    def post(self,request,*args,**kwargs):
        mid=kwargs.get('id')
        mov=Movie.objects.get(id=mid)
        user=request.user
        Favourite.objects.create(movie=mov,user=user)
        return redirect('favlist')
    
class FavouriteListView(ListView):

    template_name='favourite.html'
    context_object_name='fav'

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)