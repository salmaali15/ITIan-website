from django.urls import path
from .views import addTrainee,updateTrainee,traineeList,deleteTrainee
urlpatterns = [
   path('add_trainee',addTrainee,name='addt'),
   path('trainee_list',traineeList ,name='t_list'),
   path('update_trainee/<int:id>',updateTrainee,name='updatet'),
   path('delete_trainee/<int:id>',deleteTrainee,name='deletet'),
]
