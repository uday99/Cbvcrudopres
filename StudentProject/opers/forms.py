from django import forms

from .models import StudentModel


gen=[('Male',"Male"),('Female',"Female"),('Others',"Others")]
class StudentForm(forms.Form):
    rno = forms.IntegerField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    father_name = forms.CharField(max_length=50)
    gender=forms.ChoiceField(widget=forms.Select,choices=gen)
    course = forms.CharField(max_length=80)
    address = forms.CharField(widget=forms.Textarea)

