from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password1', 'password2']
       


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control p-3 rounded-3 mt-2",
                "required": "true",
                "id": "oldPass",
            },
            render_value=True,
        ),
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control p-3 rounded-3 mt-2",
                "required": "true",
                "id": "newPass",
            },
            render_value=True,
        ),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control p-3 rounded-3 mt-2",
                "required": "true",
                "id": "confirmPass",
            },
            render_value=True,
        ),
    )