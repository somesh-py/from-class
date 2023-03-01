from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [

    path('', views.add_show,name="addandshow"),
    path('delete/<int:id>/', views.delete_data,name="deletedata"),
    path('<int:id>/', views.update_data,name="updatedata"),

]
