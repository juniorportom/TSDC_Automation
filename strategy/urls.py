from django.urls import path
from strategy.views.application import ApplicationCreate, ApplicationList, ApplicationEdit, ApplicationDelete, ApplicationDetail
from strategy.views.applicationVersion import ApplicationVersionCreate, ApplicationVersionEdit, ApplicationVersionDelete
from strategy.views.testStrategy import TestStrategyCreate, TestStrategyList, TestStrategyEdit, TestStrategyDelete, TestStrategyDetail
from strategy.views.testPlan import TestPlanCreate, TestPlanEdit, TestPlanDelete
from strategy.views.applicationScript import ApplicationScriptCreate, ApplicationScriptEdit, ApplicationScriptDelete
from strategy.views.testExecution import executionFind, re_execute
from strategy.views.vrtTest import applications_vrt, load_scripts, load_execs, load_steps

urlpatterns = [
    path('create-application/', ApplicationCreate.as_view(), name='create-application'),
    path('application-list/', ApplicationList.as_view(), name='application-list'),
    path('edit-application/<int:pk>', ApplicationEdit.as_view(), name='edit-application'),
    path('delete-application/<int:pk>', ApplicationDelete.as_view(), name='delete-application'),
    path('detail-application/<int:pk>', ApplicationDetail.as_view(), name='detail-application'),
    path('create-application-version/<int:application_id>', ApplicationVersionCreate.as_view(), name='create-application-version'),
    path('edit-application-version/<int:application_id>/<int:pk>', ApplicationVersionEdit.as_view(), name='edit-application-version'),
    path('delete-application-version/<int:application_id>/<int:pk>', ApplicationVersionDelete.as_view(), name='delete-application-version'),

    path('create-test-strategy/', TestStrategyCreate.as_view(), name='create-test-strategy'),
    path('test-strategy-list/', TestStrategyList.as_view(), name='test-strategy-list'),
    path('edit-test-strategy/<int:pk>', TestStrategyEdit.as_view(), name='edit-test-strategy'),
    path('delete-test-strategy/<int:pk>', TestStrategyDelete.as_view(), name='delete-test-strategy'),
    path('detail-test-strategy/<int:pk>', TestStrategyDetail.as_view(), name='detail-test-strategy'),

    path('create-test-plan/<int:strategy_id>', TestPlanCreate.as_view(), name='create-test-plan'),
    path('edit-test-plan/<int:strategy_id>/<int:pk>', TestPlanEdit.as_view(), name='edit-test-plan'),
    path('delete-test-plan/<int:strategy_id>/<int:pk>', TestPlanDelete.as_view(), name='delete-test-plan'),

    path('create-application-script/<int:application_id>', ApplicationScriptCreate.as_view(), name='create-application-script'),
    path('edit-application-script/<int:application_id>/<int:pk>', ApplicationScriptEdit.as_view(), name='edit-application-script'),
    path('delete-application-script/<int:application_id>/<int:pk>', ApplicationScriptDelete.as_view(), name='delete-application-script'),

    path('execution-list/', executionFind, name='execution-list'),
    path('re-execution/<int:id_exec>', re_execute, name='re-execution'),

    path('vrt-test/', applications_vrt, name='vrt-test'),
    path('ajax/load-scripts/', load_scripts, name='ajax_load_scripts'),
    path('ajax/load-execs/', load_execs, name='ajax_load_execs'),
    path('ajax/load-steps/', load_steps, name='ajax_load_steps'),
]