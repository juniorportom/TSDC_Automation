from django.urls import path
from strategy.views.application import ApplicationCreate, ApplicationList, ApplicationEdit, ApplicationDelete, ApplicationDetail
from strategy.views.applicationVersion import ApplicationVersionCreate, ApplicationVersionEdit, ApplicationVersionDelete

urlpatterns = [
    path('create-application/', ApplicationCreate.as_view(), name='create-application'),
    path('application-list/', ApplicationList.as_view(), name='application-list'),
    path('edit-application/<int:pk>', ApplicationEdit.as_view(), name='edit-application'),
    path('delete-application/<int:pk>', ApplicationDelete.as_view(), name='delete-application'),
    path('detail-application/<int:pk>', ApplicationDetail.as_view(), name='detail-application'),
    path('create-application-version/<int:application_id>', ApplicationVersionCreate.as_view(), name='create-application-version'),
    path('edit-application-version/<int:application_id>/<int:pk>', ApplicationVersionEdit.as_view(), name='edit-application-version'),
    path('delete-application-version/<int:application_id>/<int:pk>', ApplicationVersionDelete.as_view(), name='delete-application-version'),
]