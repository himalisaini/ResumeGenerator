from django.db import models
import datetime


# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100,default="Student")
    phone_number = models.CharField(max_length=10,null=True,blank=True)
    email_id = models.CharField(max_length=300)
    dob = models.DateField(default=datetime.date.today)
    portfolio_links = models.CharField(max_length=1000)
    about_me = models.TextField(max_length=2000)
    objective = models.CharField(max_length=500)
    degree = models.CharField(max_length=100)
    field_degree = models.CharField(max_length=100,default='Field of study')
    tenth_school = models.CharField(max_length=500)
    tenth_board = models.CharField(max_length=10)
    tenth_percentage = models.CharField(max_length=10)
    twelfth_school = models.CharField(max_length=500)
    twelfth_board = models.CharField(max_length=10)
    twelfth_percentage = models.CharField(max_length=10)
    university = models.CharField(max_length=500)
    avg_cgpa = models.CharField(max_length=50)
    internship = models.TextField(max_length=2000)
    work_experience = models.TextField(max_length=2000)
    skills = models.TextField(max_length=1000)

    def __str__(self):
        return self.name