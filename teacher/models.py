from django.db import models


# Create your models here.
class Teacher(models.Model):
    teacher_id = models.AutoField(db_column='Teacher_id', primary_key=True)  # Field name made lowercase.
    teacher_name = models.CharField(db_column='Teacher_Name', max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.
    email = models.CharField(max_length=45)
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    phone = models.CharField(max_length=45)
    course = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'teacher'