from django.http import Http404
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer

# Create your views here.


class NotesList(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class GetNote(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class CreateNote(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


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
