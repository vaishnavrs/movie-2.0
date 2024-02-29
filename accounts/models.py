from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MovieCast(models.Model):
    
    options= (
            ('Actor', 'Actor'),
            ('Actress', 'Actress'),
            ('Director', 'Director'),
            ('Production','Production')                    
            )
    crew_name=models.CharField(max_length=100,blank=True,default='crew1')
    crew_type=models.CharField(max_length=100,choices=options,default='Actor')

    


    def __str__(self):
        return self.crew_name
    
    
class Movie(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    crew=models.ManyToManyField(MovieCast,related_name='movies')
    name=models.CharField(max_length=100)
    date=models.DateField()
    poster=models.ImageField(upload_to='posters')
    file=models.FileField(upload_to='video')
    options=(
        ('Action and Adventure', 'Action & Adventure'),
        ('Horror','Horror'),
        ('Comedy','Comedy'),
        ('Romance','Romance'),
        ('Science Fiction', 'Science Fiction'),
        ('Kids','kids'),
        ('Mystery and Thriller','Mystery and thriller')
    )
    type=models.CharField(max_length=256,choices=options)
    description=models.TextField()
    link=models.URLField(null=True, blank=True,max_length=500)

    def genre(self):
        type=[]
        for i,j in self.options:
            type.append(i)
        return type
    
    def __str__(self):
        return self.name
    
class Favourite(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    
