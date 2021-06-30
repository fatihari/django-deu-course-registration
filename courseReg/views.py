from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Course, Student, CoursesProgram, CollisionCourse, RegisteredCourseSchedule
import itertools

# Create your views here.



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        username = email.split("@")[0]

        if password == password2:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, 'User already exist.')            
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name, is_staff='False')
                user.save() 
                messages.success(request, 'The user record has been created successfully.')
                return redirect('login') 
        else:
            messages.error(request, 'The passwords are not the same.')
            return redirect('register')  

    else:
        return render(request,'register.html')

def login(request):  
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'Successfully logged in.')
            return redirect("/")
        else:
            messages.error(request, 'You entered incomplete or incorrect information.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request): 
    if request.method == "POST":         
        username= None
        if request.user.is_authenticated:
            username = request.user.username
        course_id_mon = [] 
        course_id_tue = []
        course_id_wed = []
        course_id_thu = []
        course_id_fri = []
        course_hour_mon = []
        course_hour_tue = []
        course_hour_wed = []
        course_hour_thu = []
        course_hour_fri = []
        course_year = []
        id_hour = []
        
        for x in range(11, 49):
            if request.POST.get('course_id_mon%s' % (x)) is not None:
                course_id_mon.insert(x,request.POST.get('course_id_mon%s' % (x)))
                if x<20:
                    course_year.insert(x,'1.Year')
                    id_hour.insert(x,x%10)
                elif x>20 and x<30:
                    course_year.insert(x,'2.Year')
                    id_hour.insert(x,x%10)                
                elif x>30 and x<40:
                    course_year.insert(x,'3.Year')
                    id_hour.insert(x,x%10)
                elif x>40:
                    course_year.insert(x,'4.Year')
                    id_hour.insert(x,x%10)
                
                if request.POST.get('course_id_mon%s' % (x))=="-":
                    course_hour_mon.insert(x, 0)
                else: 
                    course_hour_mon.insert(x, x%10)
            if request.POST.get('course_id_tue%s' % (x)) is not None:
                course_id_tue.insert(x,request.POST.get('course_id_tue%s' % (x)))
                if request.POST.get('course_id_tue%s' % (x))=="-":
                    course_hour_tue.insert(x, 0) 
                else:    
                    course_hour_tue.insert(x, x%10)
            
            if request.POST.get('course_id_wed%s' % (x)) is not None:
                course_id_wed.insert(x,request.POST.get('course_id_wed%s' % (x)))
                if request.POST.get('course_id_wed%s' % (x))=="-":
                    course_hour_wed.insert(x, 0) 
                else:    
                    course_hour_wed.insert(x, x%10)
            
            if request.POST.get('course_id_thu%s' % (x)) is not None:
                course_id_thu.insert(x,request.POST.get('course_id_thu%s' % (x)))
                if request.POST.get('course_id_thu%s' % (x))=="-":
                    course_hour_thu.insert(x, 0) 
                else:
                    course_hour_thu.insert(x, x%10)
            
            if request.POST.get('course_id_fri%s' % (x)) is not None:
                course_id_fri.insert(x,request.POST.get('course_id_fri%s' % (x)))
                if request.POST.get('course_id_fri%s' % (x))=="-":
                    course_hour_fri.insert(x, 0) 
                else:
                    course_hour_fri.insert(x, x%10)
        print(course_id_mon)
        print(course_hour_mon)
        print(course_id_mon[0])
        print(course_hour_mon[1])
        
        for x in range(len(course_id_mon)):
            courses_program = CoursesProgram(username=username, course_year=course_year[x], id_hour=id_hour[x],
            course_id_mon=course_id_mon[x],course_id_tue=course_id_tue[x], course_id_wed=course_id_wed[x],
            course_id_thu=course_id_thu[x],course_id_fri=course_id_fri[x],
            course_hour_mon=course_hour_mon[x],course_hour_tue=course_hour_tue[x],course_hour_wed=course_hour_wed[x],
            course_hour_thu=course_hour_thu[x],course_hour_fri=course_hour_fri[x])
            courses_program.save()

        return redirect('home')
    else:
        return render(request, 'home.html')

def course_registration(request):
    if request.method == "POST":

        user_id = None
        username= None
        if request.user.is_authenticated:
            user_id = request.user.id
            username = request.user.username
        
        department_name = []
        course_id = [] 
        course_name = []
        theoretical_hour = []
        practical_hour = []
        akts = []
        credit = []
        course_type = []
        branch = []
        is_course_chosen = []
        course_year = []
        for x in range(0, 32):
            department_name.insert(x,request.POST.get('department_name%s' % (x)))
            course_id.insert(x,request.POST.get('course_id%s' % (x)))
            course_name.insert(x,request.POST.get('course_name%s' % (x)))
            theoretical_hour.insert(x,request.POST.get('theoretical_hour%s' % (x)))
            practical_hour.insert(x,request.POST.get('practical_hour%s' % (x)))
            akts.insert(x,request.POST.get('akts%s' % (x)))
            credit.insert(x,request.POST.get('credit%s' % (x)))
            course_type.insert(x,request.POST.get('course_type%s' % (x)))
            branch.insert(x,request.POST.get('branch%s' % (x)))
            is_course_chosen.insert(x,request.POST.get('is_course_chosen%s' % (x)))

            if x<7:
                course_year.insert(x,'1.Year')
                
            elif x>6 and x<12:
                course_year.insert(x,'2.Year')
                              
            elif x>11 and x<17:
                course_year.insert(x,'3.Year')
                
            elif x>16:
                course_year.insert(x,'4.Year')
                
            if is_course_chosen=="on" and branch[x]=="Select": # ders seçilmiş, fakat şube seçilmemişse hata versin.
                
                return redirect('course_registration')

        student=Student(student_id=user_id,username=username)
        if not Student.objects.filter(username=username).exists():
            student.save() 
            for x in range(0,32):
                if is_course_chosen[x]=='on':
                    is_course_chosen[x]=True
                else:
                    is_course_chosen[x]=False

                if (is_course_chosen[x]==True):    
                    course=Course(username=username, course_year=course_year[x], course_id=course_id[x],department_name=department_name[x],course_name=course_name[x],theoretical_hour=theoretical_hour[x],
                    practical_hour=practical_hour[x],akts=akts[x],credit=credit[x],course_type=course_type[x],branch=branch[x],is_course_chosen=is_course_chosen[x])
                    course.save()
                    student.courses.add(course)
                   
            return redirect('collision_check')
        else:
            messages.error(request, 'ERROR: The student has already registered for the course!', extra_tags='error')
            return redirect('schedule')    
        
    else:
        return render(request, 'course_registration.html')

def collision_check(request):
    
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    
    #user_id = User.objects.get(username='admin').pk
    course = Course.objects.filter(username=username)
    n=course.count()
    
    
    control_year = []
    
    #created list for collision
    course_program_x1,course_program_x2,course_program_x3,course_program_x4,course_program_x5 = [], [], [], [], []
    course_program_y1,course_program_y2,course_program_y3,course_program_y4,course_program_y5 = [], [], [], [], []

    control_index_mon,control_index_tue,control_index_wed,control_index_thu,control_index_fri = [], [], [], [], []
    total_hour_index = [1,2,3,4,5,6,7,8]
    course_schedule_mon,course_schedule_tue,course_schedule_wed,course_schedule_thu,course_schedule_fri = [], [], [], [], []
    for x in range(n):
        
        #cme1211 var.4 tane obje var. 1, 2, 3 ve 4. saatte olmak üzere, filterde altta id ye göre alması ve eklemesi lazım
        if CoursesProgram.objects.filter(course_id_mon=course[x].course_id).exists():
            course_program_x1=CoursesProgram.objects.filter(course_id_mon=course[x].course_id)
            for i in range(len(course_program_x1)):
                course_schedule_mon.insert(course_program_x1[i].id_hour-1,course_program_x1[i])
                control_index_mon.insert(course_program_x1[i].id_hour-1,course_program_x1[i].id_hour)

        if CoursesProgram.objects.filter(course_id_tue=course[x].course_id).exists():
            course_program_x2=CoursesProgram.objects.filter(course_id_tue=course[x].course_id)
            for i in range(len(course_program_x2)):
                course_schedule_tue.insert(course_program_x2[i].id_hour-1,course_program_x2[i])
                control_index_tue.insert(course_program_x2[i].id_hour-1,course_program_x2[i].id_hour)     
            
        if CoursesProgram.objects.filter(course_id_wed=course[x].course_id).exists():
            course_program_x3=CoursesProgram.objects.filter(course_id_wed=course[x].course_id) 
            for i in range(len(course_program_x3)):
                course_schedule_wed.insert(course_program_x3[i].id_hour-1,course_program_x3[i])
                control_index_wed.insert(course_program_x3[i].id_hour-1,course_program_x3[i].id_hour)
      
        if CoursesProgram.objects.filter(course_id_thu=course[x].course_id).exists():
            course_program_x4=CoursesProgram.objects.filter(course_id_thu=course[x].course_id) 
            for i in range(len(course_program_x4)):
                course_schedule_thu.insert(course_program_x4[i].id_hour-1,course_program_x4[i])
                control_index_thu.insert(course_program_x4[i].id_hour-1,course_program_x4[i].id_hour)
            
        if CoursesProgram.objects.filter(course_id_fri=course[x].course_id).exists():
            course_program_x5=CoursesProgram.objects.filter(course_id_fri=course[x].course_id) 
            for i in range(len(course_program_x5)): 
                course_schedule_fri.insert(course_program_x5[i].id_hour-1,course_program_x5[i])
                control_index_fri.insert(course_program_x5[i].id_hour-1,course_program_x5[i].id_hour)
                
        for y in range(x+1,n):
            #x ve y. indeksli derslerin ikisi de pazartesi mi?
            if CoursesProgram.objects.filter(course_id_mon=course[y].course_id).exists() and CoursesProgram.objects.filter(course_id_mon=course[x].course_id).exists():
                course_program_y1=CoursesProgram.objects.filter(course_id_mon=course[y].course_id)
                course_program_x1=CoursesProgram.objects.filter(course_id_mon=course[x].course_id) 
                for i in range(len(course_program_x1)):
                    for j in range(len(course_program_y1)):
                        if course_program_x1[i].id_hour!=course_program_y1[j].id_hour:
                            print('Çakışma yok: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Monday - x1: ' + str(course_program_x1[i].id_hour) + ', y1:'+str(course_program_y1[j].id_hour) )
                            control_year.insert(y, True)
                        else:
                            print('Çakışma var: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Monday - x1: ' + str(course_program_x1[i].id_hour) + ', y1:'+str(course_program_y1[j].id_hour))
                            control_year.insert(y, False)
                            collision_course = CollisionCourse(username=username,course_program_monX=course_program_x1[i],
                            course_program_monY=course_program_y1[j],courseX=course[x],courseY=course[y])
                            collision_course.save()
                            


            #x ve y. indeksli derslerin ikisi de Salı mı?
            if CoursesProgram.objects.filter(course_id_tue=course[y].course_id).exists() and CoursesProgram.objects.filter(course_id_tue=course[x].course_id).exists():
                course_program_y2=CoursesProgram.objects.filter(course_id_tue=course[y].course_id)
                course_program_x2=CoursesProgram.objects.filter(course_id_tue=course[x].course_id) 
                for i in range(len(course_program_x2)):
                    for j in range(len(course_program_y2)):
                        if course_program_x2[i].id_hour!=course_program_y2[j].id_hour:
                            print('Çakışma yok: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Tuesday - x2: ' + str(course_program_x2[i].id_hour) + ', y2:'+str(course_program_y2[j].id_hour) )
                            control_year.insert(y, True)

                        else:
                            print('Çakışma var: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Tuesday - x2: ' + str(course_program_x2[i].id_hour) + ', y2:'+str(course_program_y2[j].id_hour))
                            control_year.insert(y, False)
                            collision_course = CollisionCourse(username=username,course_program_tueX=course_program_x2[i],
                            course_program_tueY=course_program_y2[j],courseX=course[x],courseY=course[y])
                            collision_course.save()


            #x ve y. indeksli derslerin ikisi de Çarşamba mı?
            if CoursesProgram.objects.filter(course_id_wed=course[y].course_id).exists() and CoursesProgram.objects.filter(course_id_wed=course[x].course_id).exists():
                course_program_y3=CoursesProgram.objects.filter(course_id_wed=course[y].course_id)
                course_program_x3=CoursesProgram.objects.filter(course_id_wed=course[x].course_id) 
                for i in range(len(course_program_x3)):
                    for j in range(len(course_program_y3)):
                        if course_program_x3[i].id_hour!=course_program_y3[j].id_hour:
                            print('Çakışma yok: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Wednesday - x3: ' + str(course_program_x3[i].id_hour) + ', y3:'+str(course_program_y3[j].id_hour ))
                            control_year.insert(y, True)


                        else:
                            print('Çakışma var: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Wednesday - x3: ' + str(course_program_x3[i].id_hour) + ', y3:'+str(course_program_y3[j].id_hour))
                            control_year.insert(y, False)
                            collision_course = CollisionCourse(username=username,course_program_wedX=course_program_x3[i],
                            course_program_wedY=course_program_y3[j],courseX=course[x],courseY=course[y])
                            collision_course.save()
    

            #x ve y. indeksli derslerin ikisi de Perşembe mi?
            if CoursesProgram.objects.filter(course_id_thu=course[y].course_id).exists() and CoursesProgram.objects.filter(course_id_thu=course[x].course_id).exists():
                course_program_y4=CoursesProgram.objects.filter(course_id_thu=course[y].course_id)
                course_program_x4=CoursesProgram.objects.filter(course_id_thu=course[x].course_id) 
                for i in range(len(course_program_x4)):
                    for j in range(len(course_program_y4)):
                        if course_program_x4[i].id_hour!=course_program_y4[j].id_hour:
                            print('Çakışma yok: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Thursday - x4: ' + str(course_program_x4[i].id_hour) + ', y3:'+str(course_program_y4[j].id_hour) )
                            control_year.insert(y, True)
                        else:
                            print('Çakışma var: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Thursday - x4: ' + str(course_program_x4[i].id_hour) + ', y4:'+str(course_program_y4[j].id_hour))
                            control_year.insert(y, False)
                            collision_course = CollisionCourse(username=username,course_program_thuX=course_program_x4[i],
                            course_program_thuY=course_program_y4[j],courseX=course[x],courseY=course[y])
                            collision_course.save()

            #x ve y. indeksli derslerin ikisi de Cuma mı?
            if CoursesProgram.objects.filter(course_id_fri=course[y].course_id).exists() and CoursesProgram.objects.filter(course_id_fri=course[x].course_id).exists():
                course_program_y5=CoursesProgram.objects.filter(course_id_fri=course[y].course_id)
                course_program_x5=CoursesProgram.objects.filter(course_id_fri=course[x].course_id) 
                for i in range(len(course_program_x5)):
                    for j in range(len(course_program_y5)):
                        if course_program_x5[i].id_hour!=course_program_y5[j].id_hour:
                            print('No Collision: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Friday - x5: ' + str(course_program_x5[i].id_hour) + ', y5:'+str(course_program_y5[j].id_hour) )
                            control_year.insert(y, True)
                        else:
                            print('Exist Collision: course x:'+course[x].course_id,'course y:'+course[y].course_id+' / Friday - x5: ' + str(course_program_x5[i].id_hour) + ', y5:'+str(course_program_y5[j].id_hour))
                            control_year.insert(y, False)
                            collision_course = CollisionCourse(username=username,course_program_friX=course_program_x5[i],
                            course_program_friY=course_program_y5[j],courseX=course[x],courseY=course[y])
                            collision_course.save()


    if False in control_year:
        print("There is a collision!")
        messages.error(request, 'ERROR: You have overlapping lessons! Please go back to the course selection screen.', extra_tags='error_collision')

          
    else:
        print("There is no collision.") # True
        messages.success(request,'There is no collision. The course selection process was successful!', extra_tags='successful') 
        
        print("perşembe mühim")
        print(course_schedule_thu)
        print(control_index_thu)
        print("perş son")


        for i in range(len(total_hour_index)):         
            #Eğer control edilen index ve total index eşit değilse örneğin control index:1,2,5,6 total index 1,2,3,4,5,6,7,8 
            while control_index_mon[i]!=total_hour_index[i]:
                
                #control indexe total indexteki "3" eklenir, yani i=2.index 
                control_index_mon.insert(i,total_hour_index[i])
                #öğrenci bu gün ve saatte(indexte) ders seçmediği için "-" eklenir, ilgili sıraya.
                course_schedule_mon.insert(i,None) 
                #şu an control: 1,2,3,5,6; total 1,2,3,4,5,6 dır eksik olan index 4'tür, bir sonraki while loopunda 4 de eklenecektir. 
                print("Pazartesi günü ders programı")
                print(control_index_mon)
                print(course_schedule_mon)
            if control_index_mon[i]==total_hour_index[i]:
                if i==len(control_index_mon)-1 and len(total_hour_index)!=len(control_index_mon):
                    course_schedule_mon.insert(i+1,None)
                    control_index_mon.insert(i+1,total_hour_index[i+1]) 

        #TUESDAY
        for i in range(len(total_hour_index)):
            while control_index_tue[i]!=total_hour_index[i]:
                control_index_tue.insert(i,total_hour_index[i])
                course_schedule_tue.insert(i,None) 
            if control_index_tue[i]==total_hour_index[i]:
                if i==len(control_index_tue)-1 and len(total_hour_index)!=len(control_index_tue):
                    course_schedule_tue.insert(i+1,None)
                    control_index_tue.insert(i+1,total_hour_index[i+1]) 
        #WEDNESDAY
        for i in range(len(total_hour_index)):
            while control_index_wed[i]!=total_hour_index[i]:
                control_index_wed.insert(i,total_hour_index[i])
                course_schedule_wed.insert(i,None) 
            if control_index_wed[i]==total_hour_index[i]:
                if i==len(control_index_wed)-1 and len(total_hour_index)!=len(control_index_wed):
                    course_schedule_wed.insert(i+1,None)
                    control_index_wed.insert(i+1,total_hour_index[i+1]) 
        #THURSDAY
        for i in range(len(total_hour_index)):
            while control_index_thu[i]!=total_hour_index[i]:
                control_index_thu.insert(i,total_hour_index[i])
                course_schedule_thu.insert(i,None) 
            if control_index_thu[i]==total_hour_index[i]:
                if i==len(control_index_thu)-1 and len(total_hour_index)!=len(control_index_thu):
                    course_schedule_thu.insert(i+1,None)
                    control_index_thu.insert(i+1,total_hour_index[i+1]) 
        #FRIDAY
        for i in range(len(total_hour_index)):
            while control_index_fri[i]!=total_hour_index[i]:
                control_index_fri.insert(i,total_hour_index[i])
                course_schedule_fri.insert(i,None) 
            if control_index_fri[i]==total_hour_index[i]:
                if i==len(control_index_fri)-1 and len(total_hour_index)!=len(control_index_fri):
                    course_schedule_fri.insert(i+1,None)
                    control_index_fri.insert(i+1,total_hour_index[i+1]) 

        for x in range(len(course_schedule_mon)):

            
            registered_course_schedule = RegisteredCourseSchedule(username=username,course_program_mon=course_schedule_mon[x],
            course_program_tue=course_schedule_tue[x], course_program_wed=course_schedule_wed[x],
            course_program_thu=course_schedule_thu[x],course_program_fri=course_schedule_fri[x])
            registered_course_schedule.save()
        return redirect('schedule')

    collison_course = CollisionCourse.objects.filter(username=username)
    collision_count = CollisionCourse.objects.filter(username=username).count()
    print(collision_count)

    #instance = SomeModel.objects.get(id=id)
    #instance.delete()


    
    student=Student.objects.filter(username=username)
    if request.method == "POST": #Eğer 'Return course selection' butonuna tıklarsa kullanıcı, tüm verileri silinsin.
        collison_course.delete()
        course.delete()
        student.delete()
        return redirect("course_registration")

    #zipped_data bir harika dostum, iki for döngüsünü aynı anda kullan keyfine bak!
    context = { 'collison_course': collison_course, 'collision_count' : range(collision_count), 'zipped_data':zip(collison_course, range(1,collision_count+1)) }
    return render(request, 'collision_check.html', context)    

def schedule(request):
    
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    #user_id = User.objects.get(username='admin').pk
    course = Course.objects.filter(username=username)
    n=course.count()
    registered_course_schedule = RegisteredCourseSchedule.objects.filter(username=username)
    countProg=registered_course_schedule.count()
    print(countProg)
    #zipped_data bir harika dostum, iki for döngüsünü aynı anda kullan keyfine bak!
    context = { 'course': course, 'registered_course_schedule':registered_course_schedule, 'n' : range(n), 'zipped_data':zip(course, range(1,n+1)),'zipped_data_program':zip(registered_course_schedule, range(1,n+19)) }
    return render(request, 'schedule.html', context)    

   

        


