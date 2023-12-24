from django.urls import path
from .views import whatsapp_redirect, index

urlpatterns = [
    path('', index, name='index'),
    path('whatsapp-redirect/', whatsapp_redirect, name='whatsapp_redirect')
]