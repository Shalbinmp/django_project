from django.db import models
from student.models import Student
from teacher.models import Teacher
# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment = models.CharField(max_length=45)
    date = models.DateField()
    #student_id = models.IntegerField(blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #teacher_id = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'payment'
