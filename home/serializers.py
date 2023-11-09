from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields=['name','age']
        # exclude=['id',]
        fields = '__all__'

    def validate(self, data):
        # check if age is less than 18
        if data['age'] < 18:
            raise serializers.ValidationError({'error': "age can't be less than 18"})
        # check if name contains numeric characters
        if data['first_name']:
            for n in data['first_name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error': 'name can not be numeric'})
        # Check for duplicate data based on name
        # existing_name = Student.objects.filter(name=data['name'])
        # if existing_name.exists():
        #     raise serializers.ValidationError({"error": "Duplicate name is not allowed..."})

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        fields=['category_name',]
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1
