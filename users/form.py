from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from company.models import Company
from resume.models import Resume

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

class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_logo', 'contact_person', 'name', 'city', 'state']
    company_logo = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                "id": "profile_pic",
                "class": "form-control p-3 rounded-3 mt-2",
                "onchange": "previewImage(this)"
            }
        )
    )

    contact_person = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "contactPerson",
                "class": "form-control p-3 rounded-3 mt-2",
            }
        )
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "companyName",
                "class": "form-control p-3 rounded-3 mt-2",
            }
        )
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "city",
                "class": "form-control p-3 rounded-3 mt-2",
            }
        )
    )

    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "country",
                "class": "form-control p-3 rounded-3 mt-2",
            }
        )
    )

class EditApplicantForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user']