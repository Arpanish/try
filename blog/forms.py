from .models import User
from django import forms

class StudentForm(forms.Form):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={
        'username':forms.TextInput(attrs={'class':"myclass",'placeholder':"Enter your username"}),
        'password':forms.PasswordInput,
        }
