from django.urls import path
from . import views

app_name = 'movies' # Namespace for URLs

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search_movies_view, name='search_movies'),
    path('movie/<str:imdb_id>/', views.movie_detail_view, name='movie_detail'),
    path('favorites/', views.favorites_view, name='favorites'),
]