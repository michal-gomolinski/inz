from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Rejestr 


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name','password')

        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

class RejestrSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Rejestr
        fields = ('pk','user','nazwa_pelna','nazwa_skrocona','dysponent_id',
                  'podstawa_prawna','przeznaczenie','zakres_info','atrybuty_liczba',
                  'obiekty_liczba')



