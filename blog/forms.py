from django import forms
from blog.models import Comment


class Comment_Form(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['post','name','subject','email','message',]