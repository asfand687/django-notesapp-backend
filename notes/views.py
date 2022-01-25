from django.http import Http404
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from .models import Note
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
