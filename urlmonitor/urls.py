# urlmonitor/urls.py

from django.urls import path
from django.contrib import admin
from monitor import views  # Make sure this import is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.url_list, name='url_list'),
    path('add/', views.add_url, name='add_url'),
]

