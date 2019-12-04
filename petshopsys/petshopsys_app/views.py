from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views import View

from .forms import LoginForm,FornecedorForm,ServicoForm,ClienteForm,PetForm,ProdutoForm,GerenteForm,VeterinarioForm,CaixaForm,EstoqueForm
from .models import Usuario,Cliente,Gerente,Caixa,Veterinario,RegistrarConsulta,Compra,Pet,ListaItemServico,ItemServico,Servico,Fornecedor,Produto,Gerente,Veterinario,Caixa,Estoque

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

def listFornecedor(request):
    #busca os dados
    fornecedores = Fornecedor.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Fornecedor.html',{'fornecedores':fornecedores})

def delFornecedor(request,pk):
    #busca os dados
    fornecedor = Fornecedor.objects.filter(pk=pk).delete()
    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return redirect('ListFornecedor')
###############################################################
def cadServico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.save()
            return redirect('MenuGerente')
    else:
        form = ServicoForm()
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

def listServico(request):
    #busca os dados
    servicos = Servico.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Servico.html',{'servicos':servicos})

def delServico(request,pk):
    #busca os dados
    servico = Servico.objects.filter(pk=pk).delete()
    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return redirect('ListServico')

####################################################################################

def cadCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        print('opa')
        if form.is_valid():
            print('oi')
            servico = form.save(commit=False)
            servico.save()
            return redirect('MenuGerente')
    else:
        form = ClienteForm()
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Cliente.html', {'form': form})

def editCliente (request,pk):
    servico = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=servico)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.save()
            return redirect('MenuGerente')
    else:
        form = ClienteForm(instance=servico)
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Cliente.html', {'form': form})

def listCliente(request):
    #busca os dados
    clientes = Cliente.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Cliente.html',{'clientes':clientes})

def delCliente(request,pk):
    #busca os dados
    cliente = Cliente.objects.filter(pk=pk).delete()
    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return redirect('ListCliente')
###########################################################################################

def cadPet(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.save()
            return redirect('MenuGerente')
    else:
        form = PetForm()
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Pet.html', {'form': form})

def editPet (request,pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            return redirect('MenuGerente')
    else:
        form = PetForm(instance=pet)
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Pet.html', {'form': form})

def listPet(request):
    #busca os dados
    pets = Pet.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Pet.html',{'pets':pets})


def delPet(request,pk):
    #busca os dados
    
    pet = Pet.objects.filter(pk=pk).delete()

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return redirect('ListPet')

###############################################################################

def cadProduto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('MenuGerente')
    else:
        form = ProdutoForm()
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Produto.html', {'form': form})

def editProduto (request,pk):
    pet = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()
            return redirect('MenuGerente')
    else:
        form = ProdutoForm(instance=pet)
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Produto.html', {'form': form})

def listProduto(request):
    #busca os dados
    produtos = Produto.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Produto.html',{'produtos':produtos})

def delProduto(request,pk):
    #busca os dados
    produto = Produto.objects.filter(pk=pk).delete()
    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return redirect('ListProduto')
###############################################################################

def cadFuncionario (request):
    return render(request,'petshopsys_app/Gerente/Cads/opcoes_Funcionario.html')

###############################################################################
def cadGerente(request):
    if request.method == "POST":
        form = GerenteForm(request.POST)
        if form.is_valid():
            gerente = form.save(commit=False)
            gerente.save()
            return redirect('MenuGerente')
    else:
        form = GerenteForm()
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Gerente.html', {'form': form})

def editGerente (request,pk):
    gerente = get_object_or_404(Gerente, pk=pk)
    if request.method == "POST":
        form = GerenteForm(request.POST, instance=gerente)
        if form.is_valid():
            gerente = form.save(commit=False)
            gerente.save()
            return redirect('MenuGerente')
    else:
        form = GerenteForm(instance=gerente)
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Gerente.html', {'form': form})

def listGerente(request):
    #busca os dados
    gerentes = Gerente.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Gerente.html',{'gerentes':gerentes})

def delGerente(request,pk):
    #busca os dados
    gerente = Gerente.objects.filter(pk=pk).delete()
    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return redirect('ListGerente')

################################################################################################

def cadVeterinario(request):
    if request.method == "POST":
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            veterinario = form.save(commit=False)
            veterinario.save()
            return redirect('MenuGerente')
    else:
        form = VeterinarioForm()
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Veterinario.html', {'form': form})

def editVeterinario (request,pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == "POST":
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            veterinario = form.save(commit=False)
            veterinario.save()
            return redirect('MenuGerente')
    else:
        form = VeterinarioForm(instance=veterinario)
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Veterinario.html', {'form': form})

def listVeterinario(request):
    #busca os dados
    veterinarios = Veterinario.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Veterinario.html',{'veterinarios':veterinarios})

def delVeterinario(request,pk):
    #busca os dados
    veterinario = Veterinario.objects.filter(pk=pk).delete()
    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return redirect('ListVeterinario')
################################################################################################

def cadCaixa(request):
    if request.method == "POST":
        form = CaixaForm(request.POST)
        if form.is_valid():
            caixa = form.save(commit=False)
            caixa.save()
            return redirect('MenuGerente')
    else:
        form = CaixaForm()
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Caixa.html', {'form': form})

def editCaixa (request,pk):
    caixa = get_object_or_404(Caixa, pk=pk)
    if request.method == "POST":
        form = CaixaForm(request.POST, instance=caixa)
        if form.is_valid():
            caixa = form.save(commit=False)
            caixa.save()
            return redirect('MenuGerente')
    else:
        form = CaixaForm(instance=caixa)
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Caixa.html', {'form': form})

def listCaixa(request):
    #busca os dados
    caixas = Caixa.objects.all().order_by('nome')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Caixa.html',{'caixas':caixas})

def delCaixa(request,pk):
    #busca os dados
    caixa = Caixa.objects.filter(pk=pk).delete()
    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return redirect('ListCaixa')
################################################################################################

def cadEstoque(request):
    if request.method == "POST":
        form = EstoqueForm(request.POST)
        if form.is_valid():
            estoque = form.save(commit=False)
            estoque.save()
            return redirect('MenuGerente')
    else:
        form = EstoqueForm()
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Estoque.html', {'form': form})

def editEstoque (request,pk):
    estoque = get_object_or_404(Estoque, pk=pk)
    if request.method == "POST":
        form = EstoqueForm(request.POST, instance=estoque)
        if form.is_valid():
            estoque = form.save(commit=False)
            estoque.save()
            return redirect('MenuGerente')
    else:
        form = EstoqueForm(instance=estoque)
    return render(request, 'petshopsys_app/Gerente/Cads/cad_Estoque.html', {'form': form})

def listEstoque(request):
    #busca os dados
    estoque = Estoque.objects.all().order_by('quantidade')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'petshopsys_app/Gerente/Cads/list_Estoque.html',{'estoque':estoque})

def delEstoque(request,pk):
    #busca os dados
    estoque = Estoque.objects.filter(pk=pk).delete()
    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return redirect('ListEstoque')