"""为应用程序users定义URL模式。"""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    # 包含默认的身份验证URL。
    path('', include('django.contrib.auth.urls')),
    # 登陆
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # 登出
    path('login', views.logout_view, name='logout'),
    # 注册页面
    path('register/', views.register, name='register'),
]