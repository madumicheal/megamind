import self
from rest_framework import serializers

from account.models import User

class RegistrationSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        User.set_password(password)
        User.save()




