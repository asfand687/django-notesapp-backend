from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ReadOnlyField
from .models import Note
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    notes = PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'notes', 'owner']


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
