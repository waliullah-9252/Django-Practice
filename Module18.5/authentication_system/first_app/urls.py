from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home , name = 'homepage'),
    path('signup/', views.sign_up , name = 'sign_up'),
    path('login/', views.user_login , name = 'user_login'),
    path('logout/', views.user_logout , name = 'user_logout'),
    path('profile/', views.user_profile , name = 'user_profile'),
    path('user_change_data/', views.user_change_data , name = 'user_change_data'),
    path('password_change/', views.password_change , name = 'password_change'),
    path('password_change2/', views.password_change2 , name = 'password_change2'),
]