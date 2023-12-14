from django.urls import path
from . views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('allapps/', index, name='allapps'),
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
   #path('delete/', delete, name='delete'),
]