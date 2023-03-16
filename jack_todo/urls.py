"""jack_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_todo, name='get_todo'),
    path('add/', views.add_todo, name='add'),
    path('edit/<item_id>', views.edit_todo, name="edit"),
    path('toggle/<item_id>', views.toggle_todo, name="toggle"),
    path('del/<item_id>', views.del_todo, name="del"),
]
