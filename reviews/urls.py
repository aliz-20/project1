from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('create/', views.review_create, name='review_create'),
    path('<int:pk>/edit/', views.review_edit, name='review_edit'),
    path('<int:pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:pk>/reply/', views.reply_create, name='reply_create'),
    path('reply/<int:pk>/edit/', views.reply_edit, name='reply_edit'),
    path('reply/<int:pk>/delete/', views.reply_delete, name='reply_delete'),
]