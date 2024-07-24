from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            "first_name",
            "last_name",
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            user = CustomUser(email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError("Passwords do not match")


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
