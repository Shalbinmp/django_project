from django.db import models
from student.models import Student
from teacher.models import Teacher

# Create your models here.
class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    request = models.CharField(max_length=45)
    #student_id = models.IntegerField(blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #teacher_id = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'request'
