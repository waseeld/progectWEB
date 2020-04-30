from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('GetHelp/', views.gethelp, name='gethelp'),
    path('PrivacyPolicy/', views.privacypolicy, name='privacypolicy'),
    path('Taxes/', views.taxes, name='taxes'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('ContactUs/', views.contactus, name='contactus'),
    path('SelectCar/', views.selectcar, name='selectcar'),
    path('OrderPage/', views.orderpage, name='orderpage'),
    path('signin/', auth_views.LoginView.as_view(template_name='home/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='home/signout.html'), name='signout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='home/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetView.as_view(template_name='home/password_reset_complete.html'),
         name='password_reset_complete'),
    path('signup/', views.signup, name='signup'),
    path('location/', views.location, name='location'),
    path('ourlocation/', views.ourlocation, name='ourlocation'),
    path('style_loc/', views.style_loc, name='style_loc'),
    path('orderform/', views.orderform, name='orderform'),

]
