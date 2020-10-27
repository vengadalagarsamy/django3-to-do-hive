"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path
from todo import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('current/', views.current, name='current'),
    # path('todo/<int:pk>/complete', views.complete, name='complete'),
    #auth
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #crud
    path('create/', login_required(views.CreateToDo.as_view()), name='create'),
    #åpath('todo/<int:pk>', views.viewtodo.as_view(), name='viewtodo'),
    path('todo/<int:pk>/update', login_required(views.updatetodo.as_view()), name='updatetodo'),
    path('todo/<int:pk>/delete', login_required(views.deletetodo.as_view()), name='deletetodo'),
    #complete
]
