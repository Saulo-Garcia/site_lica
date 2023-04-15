from django import forms
from django.forms import ModelForm
from .models import Client

class FormClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
    #     widgets={
    #         'nome': forms.TextInput(attrs={
    #             'class': 'form-login','placeholder': 'Digite seu Nome'
    #         }),
    #         'email': forms.EmailInput(attrs={
    #             'class': 'form-login','placeholder': 'Digite seu Email'
    #         })
    # } 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-login', 'placeholder': 'Digite seu Nome Completo' })
        self.fields['sobrenome'].widget.attrs.update({'class': 'form-login', 'placeholder': 'Digite seu sobrenome' })
        self.fields['email'].widget.attrs.update({'class': 'form-login', 'placeholder': 'Digite seu nome@email.com', 'size': '40' })
        self.fields['cpf'].widget.attrs.update({'class': 'form-login', 'placeholder': '___.___.___-__' })
        self.fields['nrTelCelular'].widget.attrs.update({'class': 'form-login', 'placeholder': 'Digite seu telefone' })

        
