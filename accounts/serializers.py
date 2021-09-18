from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

        def save(self):
            user = User(username=self.validate_data['username'],
                        email=self.validate_data['email'],
                        first_name=self.validate_data['first_name'],
                        last_name=self.validate_data['last_name']
                        )
            password = self.validate_data['password']
            password2 = self.validate_data['password2']
            if password2 != password:
                raise ValidationError({'password': 'Password not matches'})
            user.set_password(password)
            user.save()
            return user
