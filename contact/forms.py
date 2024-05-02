from django.core.exceptions import ValidationError
from django import forms
from . import models

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

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

    def clean(self):
        # cleaned_data = self.cleaned_data
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        return super().clean()
