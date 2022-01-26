from django.http import Http404
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Note
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer, UserSerializer
from django.contrib.auth.models import User


# Create your views here.

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NotesList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class GetNote(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class CreateNote(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpdateNote(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class DeleteNote(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
