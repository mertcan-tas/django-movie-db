from django.urls import path
from project.views import HomeView

urlpatterns = [
    path('', HomeView, name='home')
]
