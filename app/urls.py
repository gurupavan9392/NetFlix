from django.urls import path
from app.views import *
app_name='app'
urlpatterns=[
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('index/',index,name='index'),
    path('genre/<str:pk>',genre,name='genre'),
    path('my_list/',my_list,name='my_list'),
    path('search/',search,name='search'),
    path('movie/<str:pk>',movie,name='movie'),
    path('add_to_list/',add_to_list,name='add_to_list')
    
]