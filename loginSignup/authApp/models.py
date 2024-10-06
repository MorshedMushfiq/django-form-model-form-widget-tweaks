from django.db import models

# Create your models here.

class StudentModel(models.Model):
    username = models.CharField(max_length=50, null=True)
    email =  models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)
    dept = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return f"{self.username} - {self.dept}"


