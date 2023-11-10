from django.urls import path
from .views import *

urlpatterns = [
    path('student/',StudentAPI.as_view()),
    # path('get-student/', get_student, name='get_student'),
    # path('student/', post_student, name="post_student"),
    # path('update-student/<id>/', update_student, name="update_student"),
    # # path('delete_student/<id>/', delete_student,name="delete_student"),
    # path('delete_student/', delete_student, name="delete_student"),  # this is for query delete
    path('get-book/', get_book),
    path('register/',RegisterUser.as_view()),

    path('generic-student/',StudentGeneric.as_view()),
    path('generic-student/<id>/',StudentGenericUpdateAndDelete.as_view()),
]
