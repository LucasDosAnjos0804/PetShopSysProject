from django import forms
from .models import Usuario,Fornecedor,Servico,Cliente



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