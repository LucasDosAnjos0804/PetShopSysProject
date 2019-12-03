from django import forms
from .models import Usuario,Fornecedor,Servico,Cliente,Pet,Produto,Gerente,Veterinario,Caixa



class LoginForm (forms.Form):
    
    cpf = forms.CharField (label = 'CPF',max_length = 11,
        widget = forms.TextInput(
            attrs={
                'class':'form-control'
                }
            ))

    senha = forms.CharField (
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
                }
            ))
    class Meta :
        model = Usuario
            
class FornecedorForm (forms.ModelForm):
    class Meta :
        model = Fornecedor
        fields = ('cnpj','nome','endereco','telefone',)

class ServicoForm (forms.ModelForm):
    class Meta :
        model = Servico
        fields = ('nome','preco',)

class ClienteForm (forms.ModelForm):
    class Meta :
        model = Cliente
        fields = ('cpf','senha','nome','telefone','endereco')

class PetForm (forms.ModelForm):
    class Meta :
        model = Pet
        fields = ('cpf_dono','nome','tipo')

class ProdutoForm (forms.ModelForm):
    class Meta :
        model = Produto
        fields = ('cod_fornecedor','nome','data_de_validade','preco')

class GerenteForm (forms.ModelForm):
    class Meta :
        model = Gerente
        fields = ('cpf','senha','nome','telefone','endereco','telefone')

class VeterinarioForm (forms.ModelForm):
    class Meta :
        model = Veterinario
        fields = ('cpf','senha','nome','telefone','endereco','telefone','gerente')

class CaixaForm (forms.ModelForm):
    class Meta :
        model = Caixa
        fields = ('cpf','senha','nome','telefone','endereco','telefone','gerente')