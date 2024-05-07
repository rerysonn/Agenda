from django.core.exceptions import ValidationError
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForms(forms.ModelForm):

    first_name = forms.CharField(
        label= 'Primeiro Nome',
        widget= forms.TextInput(
            attrs= {
                'class' : 'classe-a classe-b',
                'placeholder' : 'Escreva o primeiro nome'
            }
        )
    )
    last_name = forms.CharField(
        label= 'Ultimo Nome',
        widget= forms.TextInput(
            attrs= {
                'class' : 'classe-a classe-b',
                'placeholder' : 'Escreva o ultimo nome'
            }
        )
    )
    phone = forms.CharField(
        label= 'Telefone',
        widget= forms.TextInput(
            attrs= {
                'class' : 'classe-a classe-b',
                'placeholder' : 'Escreva o telefone'
            }
        )
    )
    email = forms.EmailField(
        label= 'Email',
        widget= forms.TextInput(
            attrs= {
                'class' : 'classe-a classe-b',
                'placeholder' : 'Escreva o email'
            }
        )
    )
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                'accept' : 'image/*'
            }
        )
    )



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'category',
            'description',
            'picture'
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome deve ser diferente do segundo nome',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Erro',
                    code='invalid'
                )
            )
        return first_name
    
class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label= 'Primeiro nome',
        required= True,
        min_length=2
    )
    last_name = forms.CharField(
        label= 'Ultimo nome',
        required= True,
        min_length=2
    )
    email = forms.EmailField(
        required= True,
        min_length=2
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('email existente', code='invalid')
            )
        