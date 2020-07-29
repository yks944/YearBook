from django.contrib import admin
from .models import TeacherEvents,StudentEvents
# Register your models here.
admin.site.register(TeacherEvents)
admin.site.register(StudentEvents)
