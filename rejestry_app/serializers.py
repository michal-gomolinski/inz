from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BlogPost, Pet, Rejestr 


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

class BlogPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = BlogPost
        fields = ('id', 'user', 'date', 'body')


class PetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Pet
        fields = ('name', 'description', 'user', 'species')

class RejestrSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Rejestr
        fields = ('user','nazwa_pelna','nazwa_skrocona','dysponent_id',
                  'podstawa_prawna','przeznaczenie','zakres_info','zakres_lista')



