from django.urls import path
from . import views

from notes import views as notes_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup/smart/notes/', notes_views.NotesListView.as_view(), name='notes.list'),
    path('smart/notes/', notes_views.NotesListView.as_view(), name='notes.list'),
]