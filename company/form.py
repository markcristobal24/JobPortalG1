from django import forms
from .models import Company

class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['user', ]

class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_logo', 'contact_person', 'name', 'city', 'state']
    company_logo = forms.ImageField(
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