from django.urls import path
from . import views

app_name = 'practice'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:quiz_id>/calificar/', views.calificar, name='calificar'),
  path('<int:quiz_id>/', views.quiz_view, name='quiz_view'),
]
