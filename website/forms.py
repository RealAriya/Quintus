from django import forms
from website.models import Contact



class Contact_Form(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'subject': forms.TextInput(attrs={'required': False}), 
        }

