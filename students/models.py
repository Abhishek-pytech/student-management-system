from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.IntegerField()

    course = models.CharField(max_length=100)

    age = models.IntegerField()

    photo = models.ImageField(
        upload_to='students/',
        default='default.png'
    )

    def __str__(self):
        return self.name


class Attendance(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)

    status = models.CharField(max_length=10)

    def __str__(self):
        return self.student.name