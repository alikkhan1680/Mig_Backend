from rest_framework import serializers
from .models import Category, CustemUser, Direction, Course, Elon




class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustemUser
        fields = ['id', 'username', 'password', 'email']




class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        depth = 2
        fields = '__all__'


class DirectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        depth = 1
        fields = '__all__'

class ElonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Elon
        fields = '__all__'
