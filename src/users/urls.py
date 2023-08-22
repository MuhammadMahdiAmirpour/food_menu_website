from . import views
from django.urls import path

app_name = "users"
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profilepage, name="profile"),
]

