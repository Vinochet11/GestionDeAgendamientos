"""
URL configuration for STK project.

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
from templates.core.views import renderTemplate
from django.contrib.auth import views as auth_views
from templates.core import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registro/', renderTemplate),

     # auth básica
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),


    # users CRUD
    path("users/", app_views.UserList.as_view(), name="users_list"),
    path("users/<int:pk>/", app_views.UserDetail.as_view(), name="users_detail"),
    path("users/crear/", app_views.UserCreate.as_view(), name="users_create"),
    path("users/<int:pk>/editar/", app_views.UserUpdate.as_view(), name="users_update"),
    path("users/<int:pk>/eliminar/", app_views.UserDelete.as_view(), name="users_delete"),
]

