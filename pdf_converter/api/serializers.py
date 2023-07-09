from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','password']
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model=student
        
        fields=['name','age']
        #exclude=['id',]
        #fields='__all__'
    
    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({'Error':'age is less than 18'})
        return data

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    return serializers.ValidationError({'error':"name can't contain digit" })
            return data

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class booksterializer(serializers.ModelSerializer):
    category =categorySerializer()
    class Meta:
        model=Book
        fields='__all__'


class Excelfiles(serializers.ModelSerializer):

    class Meta:
        model=excel_export
        fields='__all__'   