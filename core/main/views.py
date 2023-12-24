from django.shortcuts import redirect
from django.shortcuts import render

def index(request):
    # this function renders the index.html template
    return render(request, 'main/index.html')

def whatsapp_redirect(request):
    whatsapp_number = '+918009752446'
    whatsapp_link = f'https://wa.me/{whatsapp_number}'
    return redirect(whatsapp_link)