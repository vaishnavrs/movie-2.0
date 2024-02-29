from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import RegForm,LoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.


class Homeview(View):
    def get(self,request):
        return render(request,'home.html')
    

class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,'reg.html',{'form':form})
    
    def post(self,request):
        form_data=RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('index')
        else:
            for field,errors in form_data.errors.items():
                for error in errors:
                    messages.error(request,f"{field} : {error}")
            return render(request, 'reg.html', {'form': form_data})


class LoginView(View):

    def get(self,request):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request):
        form=LoginForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            user=authenticate(username=uname,password=pwd)
            if user:
                login(request,user)
                
                return redirect('index')
            else:
                messages.error(request,'inavlid username or password')
                return redirect('login')
            

