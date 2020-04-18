from django.urls import path
from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('index',views.index,name="index"),
    path('register',views.register,name='register'),
    path('userlogin',views.user_login,name='userlogin')
]
