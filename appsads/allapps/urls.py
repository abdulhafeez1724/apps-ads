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
    path('get_placement/', get_placement, name='get_placement'),
    path('save_sorted_placement/', save_sorted_placement, name='save_sorted_placement'),
    path('delete_placement/<int:id>/', delete_placement, name='delete-placement'),

    path('network/', create_network, name='network'),
    path('network/<int:id>/', create_network, name='update_network'),
    path('get_network/', get_network, name='get_network'),
    path('save_sorted_network/', save_sorted_network, name='save_sorted_network'),
    path('delete_network/<int:id>/', delete_network, name='delete-network'),

    path('source/', create_source, name='source'),
    path('create_source/', create_source, name='create_source'),
    path('get_source/', get_source, name='get_source'),
    path('save_sorted_source/', save_sorted_source, name='save_sorted_source'),
    path('update_source/<int:id>/', create_source, name='update_source'),
    path('delete_source/<int:id>/', delete_source, name='delete_source'),
    path('source/<int:id>/', create_source, name='update_source'),
    
    path('get_network_options/', get_network_options, name='get_network_options'),


]