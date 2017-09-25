from django.shortcuts import render
from django.http import HttpResponse
#from .models import Song

def home(request):
    template_name ='home.html'
 #   songs = Song().objects.all()
  #  context = {
   #     'songs':songs
    #}
    return render(request, template_name)

def contact(request):
    return render(request, 'contact.html')