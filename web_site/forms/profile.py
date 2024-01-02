from django import forms
from django.contrib.auth import get_user_model


class ProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput())
    email = forms.CharField(disabled=True, required=False, label='E-mail', widget=forms.EmailInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
        }
