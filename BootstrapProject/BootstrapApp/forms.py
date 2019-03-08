from django import forms
from .models import SignInModel,SignUpModel


class SignInForm(forms.ModelForm):
    class Meta:
        model = SignInModel
        fields = "__all__"
        widgets = {
            'PASSWORD': forms.PasswordInput()
        }

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = "__all__"
        widgets = {
            'PASSWORD': forms.PasswordInput()
        }