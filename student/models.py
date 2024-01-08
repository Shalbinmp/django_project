from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=45)
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.
    email = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    course = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'

