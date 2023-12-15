from django.urls import path
from . views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),

    path('allapps/', apps, name='allapps'),
    path('allapps/<int:id>/', apps, name='allapps'),
    path('delete_apps/<int:id>/', delete_apps, name='delete'),
    
    
    path('placement/', create_placement, name='placement'),
    path('placement/<int:id>/', create_placement, name='update-placement'),
    path('delete_placement/<int:id>/', delete_placement, name='delete-placement'),

    path('network/', create_network, name='network'),
    path('network/<int:id>/', create_network, name='update_network'),
    path('delete_network/<int:id>/', delete_network, name='delete-network'),
]