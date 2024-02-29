from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path('comment/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('comment/new/', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/edit/', views.comment_update, name='comment_update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]
