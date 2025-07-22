from django.contrib import admin
from .models import School, Teacher, Class, Student

# PUBLIC_INTERFACE
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at')
    search_fields = ('name',)

# PUBLIC_INTERFACE
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'school')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('school',)

# PUBLIC_INTERFACE
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'teacher')
    search_fields = ('name',)
    list_filter = ('school', 'teacher')

# PUBLIC_INTERFACE
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'school', 'assigned_class')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('school', 'assigned_class')
