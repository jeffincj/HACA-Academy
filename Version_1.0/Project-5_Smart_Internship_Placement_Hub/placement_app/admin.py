from django.contrib import admin
from .models import Student, Internship, Application

admin.site.register(Student)
admin.site.register(Internship)
admin.site.register(Application)