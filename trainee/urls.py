from django.urls import path
from .views import *
urlpatterns = [
   path('add_trainee',AddTrainee.as_view(),name='addt'),
   path('trainee_list',TraineeListG.as_view() ,name='t_list'),
   path('update_trainee/<int:id>',UbdateTrainee.as_view(),name='updatet'),
   path('delete_trainee/<int:pk>',DeleteTrainee.as_view(),name='deletet'),
]
