"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path("",views.index,name='index'),
    path('add_category',views.add_category,name='add_category'),
    path('add_expense',views.add_expense,name='add_expense'),
    path('edit_expense',views.edit_expense,name='edit_expense'),
    path('edit',views.edit,name='edit'),
    path('delete',views.delete,name='delete'),
    path('login',views.login,name='login'),
    path('register/',views.register,name='register'),
    path("logout_view", views.logout_view, name="logout_view"),
    path('edit_salary',views.edit_salary,name='edit_salary')
    
]
