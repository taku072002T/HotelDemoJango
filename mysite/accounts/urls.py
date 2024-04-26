from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path('signin/', views.signinView.as_view(), name='signin'),
    path('login/', views.loginView.as_view(), name='login'),
]