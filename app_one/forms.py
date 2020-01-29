from django import forms
from django.core import validators
from django.forms import ModelForm
from app_one.models import UserInfo


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your Email again:")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators =[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make Sure Emails Match")

class SignupForm(ModelForm):
    class Meta():
        model = UserInfo
        fields = ('first_name', 'last_name', 'email')
