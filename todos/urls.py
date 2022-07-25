from django.urls import path
from todos import views

urlpatterns = [
    path('createtodo', views.createtodo, name='createtodo'),
    path('alltodos', views.alltodos, name='alltodos'),
    path('deletetodo/<int:id>', views.deletetodo, name='deletetodo'),
    path('tododetails/<int:id>', views.tododetails, name='tododetails'),
    path('todoedit/<int:id>', views.todoedit, name='todoedit'),
    path('about', views.about, name='about'),
]