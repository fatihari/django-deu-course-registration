# Generated by Django 3.1.1 on 2020-09-24 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('course_year', models.CharField(max_length=10)),
                ('department_name', models.CharField(max_length=30)),
                ('course_id', models.CharField(max_length=10)),
                ('course_name', models.TextField()),
                ('theoretical_hour', models.IntegerField()),
                ('practical_hour', models.IntegerField()),
                ('branch', models.CharField(max_length=20)),
                ('credit', models.IntegerField()),
                ('akts', models.IntegerField()),
                ('course_type', models.CharField(max_length=10)),
                ('is_course_chosen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_hour', models.IntegerField()),
                ('course_year', models.CharField(max_length=10)),
                ('course_id_mon', models.CharField(max_length=10)),
                ('course_id_tue', models.CharField(max_length=10)),
                ('course_id_wed', models.CharField(max_length=10)),
                ('course_id_thu', models.CharField(max_length=10)),
                ('course_id_fri', models.CharField(max_length=10)),
                ('course_hour_mon', models.IntegerField()),
                ('course_hour_tue', models.IntegerField()),
                ('course_hour_wed', models.IntegerField()),
                ('course_hour_thu', models.IntegerField()),
                ('course_hour_fri', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('courses', models.ManyToManyField(to='courseReg.Course')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredCourseSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('course_program_fri', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday', to='courseReg.coursesprogram')),
                ('course_program_mon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday', to='courseReg.coursesprogram')),
                ('course_program_thu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday', to='courseReg.coursesprogram')),
                ('course_program_tue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday', to='courseReg.coursesprogram')),
                ('course_program_wed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday', to='courseReg.coursesprogram')),
            ],
        ),
        migrations.CreateModel(
            name='CollisionCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('courseX', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_x', to='courseReg.course')),
                ('courseY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_y', to='courseReg.course')),
                ('course_program_friX', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fridayX', to='courseReg.coursesprogram')),
                ('course_program_friY', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fridayY', to='courseReg.coursesprogram')),
                ('course_program_monX', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mondayX', to='courseReg.coursesprogram')),
                ('course_program_monY', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mondayY', to='courseReg.coursesprogram')),
                ('course_program_thuX', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursdayX', to='courseReg.coursesprogram')),
                ('course_program_thuY', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursdayY', to='courseReg.coursesprogram')),
                ('course_program_tueX', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesdayX', to='courseReg.coursesprogram')),
                ('course_program_tueY', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesdayY', to='courseReg.coursesprogram')),
                ('course_program_wedX', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesdayX', to='courseReg.coursesprogram')),
                ('course_program_wedY', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesdayY', to='courseReg.coursesprogram')),
            ],
        ),
    ]
