from django.db import models


# Create your models here.
class Student(models.Model):
    BOY = 0
    GIRL = 1
    UNKNOWN = 255
    GENDER_IN_CHOICES = (
        (BOY, 'Boy'),
        (GIRL, 'Girl'),
        (UNKNOWN, 'Unknown'),
    )
    stu_id = models.CharField(max_length=12, primary_key=True)
    stu_name = models.CharField(max_length=20)
    stu_gender = models.IntegerField(choices=GENDER_IN_CHOICES, default=UNKNOWN)
    stu_category = models.IntegerField(default=255)

    def __str__(self):
        return self.stu_name


class Examine(models.Model):
    lable = models.CharField(max_length=100)
    start_time = models.DateTimeField('start date time')
    end_time = models.DateTimeField('end date time')
    average = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    highest_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    lowest_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    first_quartile = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    median = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    third_quartile = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)

    def __str__(self):
        return self.lable

class Score(models.Model):
    exam = models.ForeignKey(Examine, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.student.__str__() + '@' + self.exam.__str__()+ '=' + str(self.score)