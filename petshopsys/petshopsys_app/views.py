from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Usuario

# Create your views here.


def login(request):
    return render(request,'petshopsys_app/login.html')

def menu_cliente(request):
    return HttpResponse("Aqui vem o menu do cliente")

def menu_gerente(HttpResponse):
    return HttpResponse("Aqui vem o menu do genrente")

def menu_caixa(request):
    return HttpResponse("Aqui vem o menu do caixa")

def menu_veterinario(request):
    return HttpResponse("Aqui vem o menu do veterinario")
    

