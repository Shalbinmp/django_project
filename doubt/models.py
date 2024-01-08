from django.db import models
from student.models import Student
from teacher.models import Teacher

# Create your models here.
class Doubt(models.Model):
    doubt_id = models.AutoField(primary_key=True)
    doubt = models.CharField(max_length=45)
    date = models.DateField()
    #student_id = models.IntegerField(blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #teacher_id = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    doubt_reply = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'doubt'
