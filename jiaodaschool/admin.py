from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Student, Examine, Score

admin.site.register(Student)
admin.site.register(Examine)
admin.site.register(Score)