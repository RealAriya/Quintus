from django import forms
from website.models import Contact
from captcha.fields import CaptchaField


class Contact_Form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'subject': forms.TextInput(attrs={'required': False}), 
        }

