
from django.urls import path

from todoapp import views

urlpatterns = [

    path('',views.index,name="index"),
    path('delete/<int:task_id>/',views.delete,name="delete"),
    path('update/<int:task_id>/',views.update,name='update'),
    path('classlist/',views.TaskListView.as_view(),name="classlist"),
    path('classdetail/<int:pk>/',views.TaskDetailView.as_view(),name='classdetail'),
    path('classupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='classupdate'),
    path("classdelete/<int:pk>/",views.TaskDeleteView.as_view(),name='classdelete')

]