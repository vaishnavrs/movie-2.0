from django.contrib import admin
from .models import Movie,MovieCast
# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieCast)