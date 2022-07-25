from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('blog/<int:id>', views.blog, name='blog'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('remove/<int:id>', views.remove, name='remove'),
    path('add', views.add, name='add'),
]