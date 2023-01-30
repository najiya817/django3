from django import forms

class AddMarkForm(forms.Form):
    mark1=forms.IntegerField(label="Enter Mark of subject1")
    mark2=forms.IntegerField(label="Enter Mark of subject2")
    mark3=forms.IntegerField(label="Enter Mark of subject3")
    mark4=forms.IntegerField(label="Enter Mark of subject4")
    mark5=forms.IntegerField(label="Enter Mark of subject5")
    def clean(self):
        cleaned_data=super().clean()
        num1=cleaned_data.get("mark1")
        num2=cleaned_data.get("mark2")
        num3=cleaned_data.get("mark3")
        num4=cleaned_data.get("mark4")
        num5=cleaned_data.get("mark5")

        if num1<0:
            msg="mark less than zero is invalid"
            self.add_error("mark1",msg)
        if num2<0:
            msg="mark less than zero is invalid"
            self.add_error("mark2",msg)
        if num3<0:
            msg="mark less than zero is invalid"
            self.add_error("mark3",msg)
        if num4<0:
            msg="mark less than zero is invalid"
            self.add_error("mark4",msg)
        if num5<0:
            msg="mark less than zero is invalid"
            self.add_error("mark5",msg)

class StudentForm(forms.Form):
    first=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter ur firtst_name"}))
    last=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"entre ur last name"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"entre ur age"}))
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={"class":"form-control","placeholder":"enter address"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"entre ur email"}))
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"entre ur phonenumber"}))
    
    def clean(self):
        cleaned_data=super().clean()
        fn=cleaned_data.get("first")
        ln=cleaned_data.get("last")
        ag=cleaned_data.get("age")
        ph=str(cleaned_data.get("phone"))
        email=cleaned_data.get("email")
        addr=cleaned_data.get("address")
        if fn==ln:
            self.add_error("last","first and last are same")

        if ag<1:
            msg="age less than zero invalid"
            self.add_error("age","age is invalid")

        if len(ph)!=10:
            self.add_error("phone","not 10")



class ViewStudent()