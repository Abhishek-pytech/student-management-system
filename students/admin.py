from django.contrib import admin
from .models import Student
# Register your models here.
# admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone', 'course', 'age')

    search_fields = ('name', 'email', 'course')

    list_filter = ('course',)

    ordering = ('name',)

    list_per_page = 10


admin.site.register(Student, StudentAdmin)

admin.site.site_header = "Student Management Admin"
admin.site.site_title = "SMS Admin"
admin.site.index_title = "Welcome to Student Management System"