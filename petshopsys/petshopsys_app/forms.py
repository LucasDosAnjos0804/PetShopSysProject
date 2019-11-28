from django import forms
from .models import Usuario



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
            