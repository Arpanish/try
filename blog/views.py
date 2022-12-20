from django.shortcuts import render
from .models import User
from .forms import StudentForm

def home(request):
    if request.method=='POST':
        fm= StudentForm(request.POST)
        if fm.is_valid():
            names=fm.cleaned_data['username']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            reg=User(username=names,email=email,password=password)
            reg.save()
    else:
        fm = StudentForm()
    return render(request,"blog/home.html",{'form':fm})



# Create your views here.
