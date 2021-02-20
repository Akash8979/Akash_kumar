from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Contact

def home(request):
          return render(request,'home.html')

def about(request):
          return render(request,'about.html')

def contact(request):
      if request.method =="POST":
            name = request.POST['name']
            email = request.POST['email']
            #phone = request.POST.get('lname')
            ins = Contact(name=name,email=email)
            ins.save()
            #context={
                #'variable1' : " akash is looser" ,
                #'variable2' : "ankit is great man"
                 # }
      return render(request,'contact.html')

def services(request):
          return render(request,'services.html')
