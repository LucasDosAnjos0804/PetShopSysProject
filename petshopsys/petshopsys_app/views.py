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
                    return HttpResponseRedirect('/cliente/')
                    
            elif user == 'g':
                gerente = len(Gerente.objects.filter(cpf = cpf,senha =senha))

                if gerente:
                    return HttpResponseRedirect('/gerente/')

            elif user == 'ca':
                caixa = len(Caixa.objects.filter(cpf = cpf,senha = senha))
                
                if caixa:
                    return HttpResponseRedirect('/caixa/')

            elif user == 'v':
                veterinario = len(Veterinario.objects.filter(cpf = cpf,senha = senha))
            
                if veterinario:
                    return HttpResponseRedirect('/veterinario/')
            
            return self.get(request,user)
                
    def get (self,request,user):
        self.user = user

        form = LoginForm()
        return render(request,'petshopsys_app/login.html',{'form':form})


class MenuCliente (View):
    def get (self,request):
        return render(request,'petshopsys_app/Cliente/informacoes_pet.html')

class MenuGerente (View):
    def get (self,request):
        return render(request,'petshopsys_app/Gerente/opcoes.html')

class MenuCaixa (View):
    def get (self,request):
        return render(request,'petshopsys_app/Caixa/registrar_venda.html')

class MenuVeterinario (View):
    def get (self,request):
        return render(request,'petshopsys_app/Veterinario/servicos_realizados_pet.html')
    