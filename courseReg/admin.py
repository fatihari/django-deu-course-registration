from django.contrib import admin
from . models import Course, Student, CoursesProgram, CollisionCourse, RegisteredCourseSchedule

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(CoursesProgram)
admin.site.register(CollisionCourse)
admin.site.register(RegisteredCourseSchedule)