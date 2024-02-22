from django.shortcuts import redirect, render
from django.views.generic import View
from operation.forms import personsforms
from operation.forms import BookForm
from operation.forms import EmpForm
from operation.models import Employee,Person,Student
from operation.forms import Studentform,PersonForm
from operation.models import Student



class Hai(View):

    def get(self,request):

        return render(request,"hello.html")
    

class hello(View):
    def get(self,request):
        return render(request,"good.html")
    
class name(View):
    def get(self,request):
        return render(request,"today.html")  
     
class Second(View):    
    def get(self,request):
        return render(request,"good.html")
    
    def post(self,request):
         print(request.POST)
         num1=int(request.POST.get("number1"))
         num2=int(request.POST.get("number2"))
         sum=num1+num2
         print(sum)

         return render(request,"good.html")


class Subtraction(View):
    def get(self,request):
        return render(request,"good.html")
    
    def post(self,request):
         print(request.POST)
         num1=int(request.POST.get("number1"))
         num2=int(request.POST.get("number2"))
         sub=num1-num2
         print(sub)

         return render(request,"good.html")
    


class PrimeView(View):
    def get(self, request):
        return render(request, "prime.html")

    def post(self, request):
        print(request.POST)
        num1 = int(request.POST.get("number1"))
        num2 = int(request.POST.get("number2"))

        
        num = int(request.POST.get("input_number"))

        
        is_prime = self.is_prime(num)

        return render(request, "prime.html", {"is_prime": is_prime})

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

   
class Format(View):
    def get(self,request):

        return render(request,"form.html") 
     


     #name,place,gender,salary,age
class registrationview(View):
    def get(self,request):
             
     details= personsforms()
     return render(request,"registeration.html",{"form":details})
    
    def post(self,request):
     details=personsforms(request.POST)
     return render(request,"registeration.html",{"form":details})  
    
        

class BookView(View):
    def get(self,request):
        form=BookForm()
        return render(request,"book.html",{"form":form})
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
           print(form.cleaned_data)
           
        else:
            return render(request,"book.html",{"form":form})   
        return render(request,"book.html",{"form":form})    
 

class EmpView(View):
    def get(self,request):
        form=EmpForm()
        return render(request,"emp.html",{"form":form})
    def post(self,request):
        form=EmpForm(request.POST)
        
        if form.is_valid():
           Employee.objects.create(**form.cleaned_data)
           #modelname.object.creates(value)
        else:
            print("get out")
            return render(request,"emp.html",{"form":form})   
        form=EmpForm()
        return render(request,"emp.html",{"form":form})     

class StudentView(View):
     
    def get(self,request):
        form=Studentform()
        return render(request,"stud.html",{"form":form}) 
    def post(self,request):
        print(request.POST)
        form=Studentform(request.POST)
        if form.is_valid():
           Student.objects.create(**form.cleaned_data)
           
        else:
         print("get out")
        return render(request,"stud.html",{"form":form})   
        

class PersonView(View):
    def get(self,request):
        form=PersonForm()
        return render(request,"meta.html",{"form":form}) 
    def post(self,request):
        print(request.POST)
        form=PersonForm(request.POST)
        if form.is_valid():
            form.save()
           
        else:
         print("get out")
        return render(request,"meta.html",{"form":form}) 