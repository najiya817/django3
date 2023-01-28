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
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    address=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.IntegerField()
    
    def clean(self):
        cleaned_data=super().clean()
        fn=cleaned_data.get("first_name")
        ln=cleaned_data.get("last_name")
        ag=cleaned_data.get("age")
        ph=str(cleaned_data.get("phone"))
        if fn==ln:
            self.add_error("last_name","first_name and last_name are same")

        if ag<1:
            msg="age less than zero invalid"
            self.add_error("age","age is invalid")

        if len(ph)!=10:
            self.add_error("phone","not 10")

