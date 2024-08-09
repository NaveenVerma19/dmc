from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login', views.loginpage, name='loginpage'),
    path('logout-page', views.logoutUser, name="logoutuser"),
    path('register', views.registerview, name='register'),
    
    path('addprofile', views.addprofile, name='addprofile'),
    # path('reset_passwords', views.passwordresetview, name='reset_passwords'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='reset_password.html'), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_form.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]

