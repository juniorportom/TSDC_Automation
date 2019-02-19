from django.urls import path
from strategy.views.application import ApplicationCreate

urlpatterns = [
    path('create-application/', ApplicationCreate.as_view(), name='create-application'),
]