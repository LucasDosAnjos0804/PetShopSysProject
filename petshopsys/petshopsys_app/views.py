from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views import View

from .forms import LoginForm,FornecedorForm,ServicoForm
from .models import Usuario,Cliente,Gerente,Caixa,Veterinario,RegistrarConsulta,Compra,Pet,ListaItemServico,ItemServico,Servico,Fornecedor

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

        # lo_Compra = lo_ListaItemServico = lo_ItemServico = lo_Servicos = []

        # lo_Compra.extend(
        #     Compra.objects.filter(
        #         cod_cliente = cli
        #     )
        # )
        # for o in lo_Compra:
        #     lo_ListaItemServico.extend(
        #         ListaItemServico.objects.filter(
        #             cod_item_servico=o.pk
        #     ))
        
        # for o in lo_ListaItemServico:
        #     lo_ItemServico.extend(
        #         ItemServico.objects.filter(
        #             cod_item_servico=o.pk
        #         )
        #     )

        # for o in lo_ItemServico:
        #     lo_Servicos.extend(
        #         Servico.objects.filter(
        #             cod_servico=o.pk
        #         )
        #     )
            
        # print(lo_Servicos)#printa os nomes

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


class Cad_Cliente (View):
    def get (self,request):
        return render(request,'petshopsys_app/Gerente/Cads/cad_Cliente.html')

# class CadFornecedor (View):
#     def post (self,request):
#         form = FornecedorForm(request.POST)

#         if form.is_valid():

#             fornecedor = form.save(commit=False)

#             fornecedor.save()
#             return redirect('MenuGerente')
    
#     def get (self,request):
#         form = FornecedorForm()
#         return render(request, 'petshopsys_app/Gerente/Cads/cad_Fornecedor.html', {'form': form})

def cadFornecedor (request):
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = form.save(commit=False)
            fornecedor.save()
            return redirect('MenuGerente')
    else:
        form = FornecedorForm()
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Fornecedor.html', {'form': form})

def editFornecedor (request,pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            fornecedor = form.save(commit=False)
            fornecedor.save()
            return redirect('MenuGerente')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Fornecedor.html', {'form': form})

def detFornecedor (request, pk):

    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    
    return render(request, 'petshopsys_app/Gerente/Cads/detail_Fornecedor.html', {'fornecedor': fornecedor})

def listFornecedor(request):
    #busca os dados
    fornecedores = Fornecedor.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Fornecedor.html',{'fornecedores':fornecedores})



###############################################################
def cadServico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        print('opa')
        if form.is_valid():
            print('oi')
            servico = form.save(commit=False)
            servico.save()
            return redirect('MenuGerente')
    else:
        form = ServicoForm()
        print('oi2')
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Servicos.html', {'form': form})

def editServico (request,pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == "POST":
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.save()
            return redirect('MenuGerente')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Servicos.html', {'form': form})

def detServico (request, pk):

    servico = get_object_or_404(Servico, pk=pk)
    
    return render(request, 'petshopsys_app/Gerente/Cads/detail_Servico.html', {'servico': servico})

def listServico(request):
    #busca os dados
    servicos = Servico.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Servico.html',{'servicos':servicos})

########################################################################
