from django import forms
from .models import Usuario,Fornecedor



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
    # cnpj = forms.CharField (label = 'CNPJ', max_length = 14,
    #     widget = forms.TextInput(
    #         attrs={
    #             'class':'form-control'
    #         }
    #     ))
    # nome = forms.CharField (label = 'Nome', max_length = 50,
    #     widget = forms.TextInput(
    #         attrs={
    #             'class':'form-control'
    #         }
    #     ))
    # endereco = forms.CharField (label = 'Endereco', max_length = 150,
    #     widget = forms.TextInput(
    #         attrs={
    #             'class':'form-control'
    #         }
    #     )) 
    # telefone = forms.CharField (label = 'Telefone', max_length = 14,
    #     widget = forms.TextInput(
    #         attrs={
    #             'class':'form-control'
    #         }
    #     ))

    class Meta :
        model = Fornecedor
        fields = ('cnpj','nome','endereco','telefone',)