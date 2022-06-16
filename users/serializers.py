from users.models import User
from rest_framework import fields, serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password


class SignupSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new user using signup form
    """

    class Meta:
        model = User
        fields = ['email', 'id', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validate_password(validated_data['password']) is None:
            password = make_password(validated_data['password'])
            user = User.objects.create(
                email=validated_data['email'],
                password=password
            )

        return user
