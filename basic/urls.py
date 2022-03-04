from unicodedata import name
from django.urls import path
from basic import views

app_name='basic'

urlpatterns = [
    path('register/', views.register, name='reg'),
    path('login/', views.user_login_page, name='login'),
    path('index/', views.home, name='home'),
    path('trash/', views.trash, name='login_req'),
    path('logout/', views.user_logout, name='logout'),
]