from django.urls import path
from .views import *

app_name='NATURE_CLUB'

urlpatterns = [
    path('', Home, name='Home'),
    path('About', About, name='About'),
    path('Contact', Contact, name='Contact'),
    path('Gallery', gallery, name='Gallery'),
    path('Events', events, name='Events'),
]