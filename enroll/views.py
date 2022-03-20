import email
from urllib import request
from django.shortcuts import render
from .forms import studentRegistration

# Create your views here.
def showform(request):
      if request.method == 'POST':
            fm = studentRegistration(request.POST)
            if fm.is_valid():
                  name =fm.cleaned_data['name']
                  email=fm.cleaned_data['email']
                  print('name', name)
                  print('email', email)

      else:
            fm = studentRegistration()
            print('request method')
     
      return render(request, 'enroll/registration.html',{'form':fm})