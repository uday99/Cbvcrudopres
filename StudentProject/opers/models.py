from django.db import models

# Create your models here.

class StudentModel(models.Model):
    rno=models.IntegerField(primary_key=True,unique=True)
    first_name=models.CharField(max_length=50)

    last_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    course=models.CharField(max_length=80)
    address=models.CharField(max_length=150)

