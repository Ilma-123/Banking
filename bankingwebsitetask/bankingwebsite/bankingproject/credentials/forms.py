from django import forms
from .models import Customer


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'dob', 'age', 'gender', 'contact_number', 'email', 'address']


class BranchForm(forms.Form):
    District = forms.CharField(label='Select a District', max_length=100)
