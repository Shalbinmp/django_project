from django.db import models
from teacher.models import Teacher
# Create your models here.
class StudyMaterial(models.Model):
    studymaterial_id = models.AutoField(primary_key=True)
    study_material = models.CharField(max_length=45)
    date = models.DateField()
    #teacher_id = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=45)
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'study_material'