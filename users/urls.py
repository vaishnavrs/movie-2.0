from django.urls import path
from .views import *


urlpatterns=[
    path('ind',IndexView.as_view(),name='index'),
    path('mdetail/<int:id>',MovieDetailView.as_view(),name= 'movie-detail'),
    path('watch/<int:id>',PlayVideoView.as_view(),name='watchnow'),
    path('profile',ProfileView.as_view(),name='profile'),
    path('upload',UploadMovieView.as_view(),name='upload'),
    # path('update/<int:id>',ProfileEditView.as_view(),name='pedit'),
    path('search',SearchView.as_view(),name='search'),
    path('medit/<int:id>',MovieUpdateView.as_view(),name='mupdate'),
    path('mdelete/<int:id>',MovieDeleteView.as_view(),name='delete'),
    path('movies/<str:cat>',CategoryView.as_view(),name='category'),
    path('fav/<int:id>',AddToFavouriteView.as_view(),name='fav'),
    path('favlist',FavouriteListView.as_view(),name='favlist')
]
