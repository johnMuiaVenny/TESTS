from django.urls import path
from .views import *

app_name='NATURE_CLUB'

urlpatterns = [
    path('', Home, name='Home'),
    path('About', About, name='About'),
    path('Contact', Contact, name='Contact'),
    path('Gallery', gallery, name='Gallery'),
    path('Events', events, name='Events'),
    path('Subcom1', Subcom1, name='Subcom1'),
    path('Subcom2', Subcom2, name='Subcom2'),
    path('Subcom3', Subcom3, name='Subcom3'),
]