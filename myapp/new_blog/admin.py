from django.contrib import admin
from .models import School, Grade, Certificate_type, Faculty, Department, Student

admin.site.register(School)
admin.site.register(Grade)
admin.site.register(Certificate_type)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Student)

# Register your models here.
