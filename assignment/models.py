from django.db import models
from teacher.models import Teacher

# Create your models here.

class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    assignment = models.CharField(max_length=100)
    date = models.DateField()
    #teacher_id = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    submission_date = models.DateField()
    subject = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'assignment'
