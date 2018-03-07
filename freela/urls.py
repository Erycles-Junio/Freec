from django.contrib.auth.views import logout
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('inicio/', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('register_project/', views.register_project, name='register_project'),
    path('project_details/<int:pid>/', views.project_details, name='project_details'),
    path('enviroment/<int:eid>/', views.enviroment_view, name='enviroment'),
    path('services/', views.services_view, name='services'),
    path('my_projects/', views.my_projects, name='myprojects'),
    path('delete_project/<int:pk>', views.delete_project, name='delete_project'),
    path('update_project/<int:pk>', views.update_project, name='update_project'),
    path('send_message/<int:receiver>/<int:sender>/', views.send_message, name='send_message'),
    path('messages/', views.message_list, name='message_list'),
    path('delete_message/<int:pk>', views.delete_message, name='delete_message'),

]
