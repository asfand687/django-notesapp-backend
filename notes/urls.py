from django.urls import path, include
from . import views

urlpatterns = [
    path('notes/', views.NotesList.as_view(), name="get-notes"),
    path('notes/create/', views.CreateNote.as_view(), name="create-note"),
    path('notes/<str:pk>/', views.GetNote.as_view(), name="get-note"),
    path('notes/<str:pk>/delete/', views.DeleteNote.as_view(), name="delete-note"),
    path('notes/<str:pk>/update/', views.UpdateNote.as_view(), name="update-note"),
    path('users/', views.UserList.as_view(), name="get-users"),
    path('users/<str:pk>/', views.GetUser.as_view(), name="get-user"),
    path('hello/', views.HelloView.as_view(), name='hello'),
]
