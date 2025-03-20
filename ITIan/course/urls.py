from django.urls import path
from .views import addCourse, updateCourse, courseList, deleteCourse

urlpatterns = [
    path('add_course', addCourse, name='addc'),
    path('course_list', courseList, name='c_list'),
    path('update_course/<int:id>', updateCourse, name='updatec'),
    path('delete_course/<int:id>', deleteCourse, name='deletec'),
]
