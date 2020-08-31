from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start-quiz', views.takeQuiz, name='take-quiz'),
    path('result/<int:pk>', views.result, name='result')

]
