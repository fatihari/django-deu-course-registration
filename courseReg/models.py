from django.db import models

# Create your models here.

class Course(models.Model):
    username=models.CharField(max_length=30)
    course_year = models.CharField(max_length=10) # 1.Year, 2.Year, 3.Year, 4.Year
    department_name = models.CharField(max_length=30) #Computer Engineering
    course_id = models.CharField(max_length=10) # CME4401
    course_name = models.TextField() #Applications of Decision Support Systems
    theoretical_hour = models.IntegerField() #2 hour
    practical_hour = models.IntegerField() # 2 hour
    branch = models.CharField(max_length=20) # 1 or 2. branch
    credit = models.IntegerField() # 3 credit
    akts = models.IntegerField() # 6 akts
    course_type = models.CharField(max_length=10) #compulsory or elective
    #total_hour = models.IntegerField() # if total_hour<26 hour, it will be occur. 
    is_course_chosen = models.BooleanField(default=False) # True or False

    def __str__(self):
        return str(self.username+'-'+self.course_name)
    objects = models.Manager()
    
class Student(models.Model):
    student_id = models.IntegerField() # equal user.id
    username = models.CharField(max_length=30) #equal user.username
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return str(self.username)
    objects = models.Manager()

class CoursesProgram(models.Model):
    id_hour = models.IntegerField() #1.Hour, 2.Hour, 3.Hour
    course_year = models.CharField(max_length=10) # 1.Year, 2.Year, 3.Year, 4.Year
    course_id_mon = models.CharField(max_length=10) # CME4401
    course_id_tue = models.CharField(max_length=10)
    course_id_wed = models.CharField(max_length=10)
    course_id_thu = models.CharField(max_length=10)
    course_id_fri = models.CharField(max_length=10)
    course_hour_mon = models.IntegerField() # equal from 1 to 8 hour
    course_hour_tue = models.IntegerField()
    course_hour_wed = models.IntegerField()
    course_hour_thu = models.IntegerField()
    course_hour_fri = models.IntegerField()
    username=models.CharField(max_length=30)
    def __str__(self):
        return str(self.course_year+" - "+str(self.id_hour) + ".Hour")
    objects = models.Manager()

class CollisionCourse(models.Model):
    courseX = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_x')
    courseY = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_y')
    course_program_monX = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='mondayX')
    course_program_tueX = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='tuesdayX')
    course_program_wedX = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='wednesdayX')
    course_program_thuX = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='thursdayX')
    course_program_friX = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='fridayX')
    course_program_monY = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='mondayY')
    course_program_tueY = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='tuesdayY')
    course_program_wedY = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='wednesdayY')
    course_program_thuY = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='thursdayY')
    course_program_friY = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='fridayY')
    username = models.CharField(max_length=30)

    def __str__(self):
        # pylint: disable=E1101
        courseXName = self.courseX.course_name
        courseYName = self.courseY.course_name
        return f'{courseXName} - {courseYName}'
    
    objects = models.Manager()

class RegisteredCourseSchedule(models.Model):
    #id_hour = models.IntegerField(primary_key=True)
    
    course_program_mon = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='monday')
    course_program_tue = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='tuesday')
    course_program_wed = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='wednesday')
    course_program_thu = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='thursday')
    course_program_fri = models.ForeignKey(CoursesProgram, on_delete=models.CASCADE, null=True, related_name='friday')
    username = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.username)
    objects = models.Manager()
    
    