from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Internship(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    skills = models.TextField()

    def __str__(self):
        return self.role
    
class Application(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship,on_delete=models.CASCADE)

    status = models.CharField(
        max_length=50,
        default="Processing"
    )

    feedback = models.TextField(
        default="Application Under Review"
    )

    def __str__(self):
        return self.status