from django.urls import path
from . views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('allapps/', index, name='allapps'),
    path('create/', create_apps, name='create'),
    path('update/<int:id>/', update_apps, name='update'),
    path('delete_apps/<int:id>/', delete_apps, name='delete'),
    path('placement/', placement, name='placement'),
    path('placement/<int:id>/', update_placement, name='update-placement'),
    path('delete_placement/<int:id>/', delete_placement, name='delete-placement'),
    path('adnetwork/', AdNetwork, name='adnetwork'),
]