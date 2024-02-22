from django import forms
from operation.models import Person

class personsforms(forms.Form):
    name=forms.CharField()
    age=forms.CharField()
    gender=forms.CharField()
    
class BookForm(forms.Form):
    title=forms.CharField()
    author=forms.CharField()
    genre=forms.CharField()

class EmpForm(forms.Form):
    name=forms.CharField()
    salary=forms.CharField()
    position=forms.CharField()
    place=forms.CharField()

class Studentform(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    gender=forms.CharField()
    course=forms.CharField()

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person 
        fields='__all__'