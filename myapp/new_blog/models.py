from django.db import models
from django.db.models import CASCADE


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=30)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Certificate_type(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Grade(models.Model):
    type = models.IntegerField()

    def __str__(self):
        return self.type


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    year_of_graduation = models.IntegerField()
    department = models.ForeignKey(Department, default='1', on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, default='0', on_delete=CASCADE)
    school = models.ForeignKey(School, default='1', on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_type, default='N', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
