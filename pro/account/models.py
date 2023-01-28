from django.db import models

# Create your models here.
class TeacherModel(models.Model):
#first last phone email qualification
    first=models.CharField(max_length=100)
    last=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()
    qualification=models.CharField(max_length=100)
  