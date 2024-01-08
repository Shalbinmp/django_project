from django.db import models
from student.models import Student
from teacher.models import Teacher
# Create your models here.

class Complaints(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    date = models.DateField()
    reply = models.CharField(max_length=45, blank=True, null=True)
    # student_id = models.IntegerField(blank=True, null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    #teacher_id = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    complaints = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'complaints'




