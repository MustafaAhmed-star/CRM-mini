
from django.urls import path

from . import views0
from app.views.create_record import create_record_view
from app.views.dashboard_view import dashboard_view
from app.views.update_record_view import update_record_view

urlpatterns = [

    path('', views0.home, name=""),

    path('register', views0.register, name="register"),

    path('my-login', views0.my_login, name="my-login"),

    path('user-logout', views0.user_logout, name="user-logout"),

    # CRUD

    path('dashboard', dashboard_view, name="dashboard"),

    path('create-record', create_record_view, name="create-record"),

    path('update-record/<int:pk>',update_record_view, name='update-record'),

    path('record/<int:pk>', views0.singular_record, name="record"),

    path('delete-record/<int:pk>', views0.delete_record, name="delete-record"),

    

]






