from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustemUser(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Erkak'),
        ('Female', 'Ayol'),
    ]
    USER_STATUS = [
        ('Teacher', 'TEACHER'),

        ('Student', 'STUDENT')
    ]
    userAge = models.IntegerField(null=True, blank=True)
    userNumber = models.CharField(max_length=18, null=True, blank=True)
    userPicture = models.ImageField(upload_to="StudentImg", null=True, blank=True)
    userCash = models.FloatField(null=True)
    teacherSkills = models.CharField(max_length=200)
    userGender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    userStatus = models.CharField(max_length=10, choices=USER_STATUS)
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='custom_user_permissions')

    def __str__(self):
        return self.userStatus


class Direction(models.Model):
    directionName = models.CharField(max_length=150)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.directionName


class Category(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True, blank=True)
    catName = models.CharField(max_length=150, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.catName


class Course(models.Model):
    teachers = models.ForeignKey(CustemUser, on_delete=models.CASCADE, null=True, blank=True)
    live_time = models.DateTimeField()
    courseName = models.CharField(max_length=200, verbose_name="course_name", null=True, blank=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    descriptions = models.TextField()
    price = models.FloatField()
    course_link = models.CharField(max_length=200, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    maxStudentsCount = models.IntegerField(null=True, blank=True)
    jamgarma = models.IntegerField(null=True, blank=True, default=0)
    students_count = models.IntegerField(null=True, blank=True, default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.courseName


class Elon(models.Model):
    number = models.IntegerField(null=True, blank=True)
    elon = models.TextField(null=True, blank=True)
    elonImg = models.ImageField(upload_to='media', null=True, blank=True)

    def __int__(self):
        return self.number
