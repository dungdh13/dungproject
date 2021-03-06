"""django_project URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('loginN/', user_views.login_user, name='loginN'),
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout1/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout1'),
    path('', include('blog.urls')),
    path('sk/',user_views.sk, name='sk'),
    path('current/', user_views.currenttodos, name='currenttodos'),
    path('todo/<int:todo_pk>/delete',user_views.deletetodo, name='deletetodo'),
    path('todo/<int:todo_pk>', user_views.viewtodo, name='viewtodo'),
    path('dl/', user_views.download, name='download'),
    path('change_password/', user_views.change_password, name='change_password'),
    path('registration/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)