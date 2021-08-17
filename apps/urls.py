from django.urls import path

from apps import views

urlpatterns = [
    path('', views.CreateAppLog.as_view(), name='create_app_log')
]
