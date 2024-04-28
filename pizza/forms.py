from django import forms


class EnterForm(forms.Form):
    login = forms.CharField(label='логин')
    password = forms.CharField(label='пароль', widget=forms.PasswordInput)
