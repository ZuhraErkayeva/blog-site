from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify-email/<int:pk>/<str:token>/', views.VerifyEmail.as_view(), name='verify_email'),


]