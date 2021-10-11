from django.shortcuts import render
# starting template
from .import views

def index(request):
    return render(request,'main/index.html')

