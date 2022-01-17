from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(validators=[UniqueValidator(
    #     queryset=User.objects.all(), message=("Username already Exists..")), ])  # for test purpose(but works)

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'password', 'is_active', 'is_superuser']

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    # def validate_email(self, value):
    #     print("heyyyy")
    #     if value == "":
    #         raise serializers.ValidationError("Email cannot be null")
    #     elif User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("Email already exists")
    #     return value

    # def validate_username(self, value):
    #     print("helloooo")
    #     if value == "":
    #         raise serializers.ValidationError("Username cannot be null")
    #     elif User.objects.filter(username=value).exists():
    #         raise serializers.ValidationError("Username already exists")
    #     return value

    def validate_password(self, value):
        if value == "":
            raise serializers.ValidationError("Password cannot be null")
        return value
