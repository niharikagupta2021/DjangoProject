from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('success/', views.success_view, name='success'),
    
    path("users/", views.get_all_users),
    path("user/<str:email>/", views.get_user_by_email),
    path("user/update/<str:email>/", views.update_user),
    path("user/delete/<str:email>/", views.delete_user),
]
