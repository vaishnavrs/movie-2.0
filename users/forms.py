from accounts.models import Movie
from accounts.models import MovieCast
from django import forms
from django.contrib.auth.models import User



class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','date','poster','file','type','description','link']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'date':forms.DateInput(attrs={'class':'form-control datepicker','placeholder':'Date of release'}),
            'type':forms.Select(attrs={'class':'custom-select'}),
            'link':forms.URLInput(attrs={'class':'form-control','placeholder':'Trailer link'})

        }

class CrewForm(forms.ModelForm):
    class Meta:
        model=MovieCast
        fields=['crew_name','crew_type']  
        widgets={
            'crew_name':forms.TextInput(attrs={'class':'form-control'}),
            'crew_type':forms.Select(attrs={'class':'custom-select'})
        }

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
            'last_name':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Last Name'}),
            'email':forms.TextInput(attrs= {'class':'form-control','placeholder':'email id'} ),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            
        }
        

