from django.urls import path
from strategy.views.application import ApplicationCreate, ApplicationList, ApplicationEdit, ApplicationDelete, ApplicationDetail

urlpatterns = [
    path('create-application/', ApplicationCreate.as_view(), name='create-application'),
    path('application-list/', ApplicationList.as_view(), name='application-list'),
    path('edit-application/<int:pk>', ApplicationEdit.as_view(), name='edit-application'),
    path('delete-application/<int:pk>', ApplicationDelete.as_view(), name='delete-application'),
    path('detail-application/<int:pk>', ApplicationDetail.as_view(), name='detail-application'),
]