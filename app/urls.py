from turtle import update
from unicodedata import name
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.insertPageView, name='insertpage'),
    path('insert/', views.insertData, name='insert'),
    path('show/', views.showPageView, name='show'),
    path('edit/<int:pk>', views.editPage, name='edit'),
    path('update/<int:pk>', views.updateData, name='update'),
    path('delete<int:pk>', views.deleteData, name='delete')
]
