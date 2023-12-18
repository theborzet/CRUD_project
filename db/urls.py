"""
URL configuration for db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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




from todos.views import ModelView, TodoCreateView, delete_task, TodoUpdateView, SearchView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ModelView.as_view(), name='index'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('update_todo/<int:pk>/', TodoUpdateView.as_view(), name='update_todo'),
    path('search/', SearchView.as_view(), name='search'),
]
