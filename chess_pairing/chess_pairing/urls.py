"""
URL configuration for chess_pairing project.

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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from tournament import views
from tournament.views import register,complete_round

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tournament_list, name='tournament_list'),
    path('tournament/<int:tournament_id>/', views.tournament_detail, name='tournament_detail'),
    path('tournament/<int:tournament_id>/register/', views.register_player, name='register_player'),
    path('tournament/<int:tournament_id>/pair/', views.pair_round, name='pair_round'),
    path('round/<int:round_id>/', views.round_detail, name='round_detail'),
    path('game/<int:game_id>/submit/', views.submit_result, name='submit_result'),
    path('register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('round/<int:round_id>/complete/', complete_round, name='complete_round'),

    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html')),
    path('admin/', admin.site.urls),

]
admin.site.site_header = "Chess Tournament Admin"
admin.site.site_title = "Chess Tournament Admin Portal"
admin.site.index_title = "Welcome to Chess Tournament System"