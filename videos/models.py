from django.db import models
from teacher.models import Teacher

# Create your models here.
class Videos(models.Model):
    video_id = models.AutoField(primary_key=True)
    video = models.CharField(max_length=500, blank=True, null=True)
    #teacher_id = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'videos'

