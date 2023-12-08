from django.urls import path
from . import views

urlpatterns = [
    path('standings/', views.StandingsView.as_view()),
]
