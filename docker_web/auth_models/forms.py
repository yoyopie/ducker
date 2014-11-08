from django import forms
from web_site import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("username", "password")
        widgets = {'password': forms.PasswordInput()}
