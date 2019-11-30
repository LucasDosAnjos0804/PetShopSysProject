from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views import View

from .forms import LoginForm
from .models import Usuario,Cliente,Gerente,Caixa,Veterinario,RegistrarConsulta,Compra,Pet,ListaItemServico,ItemServico


# Create your views here.



class Index (View):
    def get (self,request):
        return render(request,'petshopsys_app/index.html')


class Login (View):
    user = None

    def post (self,request,user):
        form = LoginForm(request.POST)

        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            senha = form.cleaned_data['senha']

            if user == 'cl':
                cliente = len(Cliente.objects.filter(cpf = cpf,senha = senha))

                if cliente:
                    # return HttpResponseRedirect('/cliente/')
                    return redirect('MenuCliente',cli=cpf)
                    
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

    def get (self,request,cli):
        estrutura = []
        compras = []
        litensservico = []
        itensservico = []


        compras = Compra.objects.filter (
            cod_cliente__cpf=cli
            )

        for compra in compras:
            litensservico.extend(
                ListaItemServico.objects.filter(
                    pk=compra.cod_lista_item_servico.pk
                )
            )
        for item in litensservico:
            itensservico.extend(ItemServico.objects.filter(
                pk=item.pk
            ))
        for item in itensservico:
            print(item)
            

        # if len(consultas)>0:



        
        # return render(request,'petshopsys_app/Cliente/informacoes_pet.html',{'consultas':consultas})
        return render(request,'petshopsys_app/Cliente/informacoes_pet.html')



class MenuGerente (View):
    def get (self,request):
        return render(request,'petshopsys_app/Gerente/opcoes.html')

class MenuCaixa (View):
    def get (self,request):
        return render(request,'petshopsys_app/Caixa/opcoes-caixa.html')

class MenuVeterinario (View):
    def get (self,request):
        return render(request,'petshopsys_app/Veterinario/servicos_realizados_pet.html')
    