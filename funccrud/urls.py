from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name="home"),
    path('newblog/', views.create, name="newblog"),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('comment/<int:pk>', views.add_comment, name='add_comment'),
]