from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views import View

from .forms import LoginForm
from .models import Usuario,Cliente,Gerente,Caixa,Veterinario

# Create your views here.



class Index (View):
    def get (self,request):
        return render(request,'petshopsys_app/index.html')

class Login (View):
    user = None

    def post (self,request,user):
        form = LoginForm(request.POST)

        print('if do post')
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            senha = form.cleaned_data['senha']

            if user == 'cl':
                cliente = len(Cliente.objects.filter(cpf = cpf,senha = senha))

                if cliente:
                    return HttpResponseRedirect('Uhuuuu! Cliente')
                    
            elif user == 'g':
                gerente = len(Gerente.objects.filter(cpf = cpf,senha =senha))

                if gerente:
                    return HttpResponseRedirect('Uhuuuu! Gerente')

            elif user == 'ca':
                caixa = len(Caixa.objects.filter(cpf = cpf,senha = senha))
                
                if caixa:
                    return HttpResponseRedirect('Uhuuuu! Caixa')

            elif user == 'v':
                veterinario = len(Veterinario.objects.filter(cpf = cpf,senha = senha))
            
                if veterinario:
                    return HttpResponseRedirect('Uhuuuu! Veterinario')
            
            return self.get(request,user)
                
    def get (self,request,user):
        self.user = user

        form = LoginForm()
        return render(request,'petshopsys_app/login.html',{'form':form})


def menu_cliente(request):
    return HttpResponse(request,'petshopsys_app/informações-pet.html')

def menu_gerente(HttpResponse):
    return HttpResponse("Aqui vem o menu do genrente")

def menu_caixa(request):
    return HttpResponse("Aqui vem o menu do caixa")

def menu_veterinario(request):
    return HttpResponse("Aqui vem o menu do veterinario")


