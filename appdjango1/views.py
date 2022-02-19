from django.shortcuts import render
from .models import Usuarios
from django.http import HttpResponse


# Create your views here.
def index(request):
    users = Usuarios.objects.all()
    context = {
        'users': users
    }
    return render(request, 'appdjango1/index.html', context)
