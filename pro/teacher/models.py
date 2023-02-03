from django.db import models

# Create your models here.
class StudentModel(models.Model):
    first=models.CharField(max_length=100)
    last=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    image=models.ImageField(upload_to="student_images",null=True)
  
    