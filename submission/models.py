from django.db import models
from student.models import Student
from assignment.models import Assignment



# Create your models here.
class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
   # assignment_id = models.IntegerField(blank=True, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    #student_id = models.IntegerField(blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.CharField(max_length=100)

    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'submission'
