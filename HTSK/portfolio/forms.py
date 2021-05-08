from .models import Order
from django.forms import ModelForm, TextInput, FileInput, EmailInput, Textarea


class OrderForm(ModelForm):
    class Meta:
        model = Order

        fields = ['surname', 'name', 'description', 'email', 'files']

        widgets = {
            "surname": TextInput(attrs={
                'placeholder': 'Фамилия'
            }),
            "name": TextInput(attrs={
                'placeholder': 'Имя'
            }),
            "description": Textarea(attrs={
                'placeholder': 'Описание заказа'
            }),
            "email": EmailInput(attrs={
                'placeholder': 'email'
            }),
            "files": FileInput()
        }