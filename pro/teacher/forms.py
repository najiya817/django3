from django import forms

class AddMarkForm(forms.Form):
    mark1=forms.IntegerField(label="Enter Mark of subject1")
    mark2=forms.IntegerField(label="Enter Mark of subject2")
    mark3=forms.IntegerField(label="Enter Mark of subject3")
    mark4=forms.IntegerField(label="Enter Mark of subject4")
    mark5=forms.IntegerField(label="Enter Mark of subject5")

class StudentForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    address=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.IntegerField()

