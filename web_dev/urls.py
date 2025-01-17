# Inside web_dev/urls.py
from django.urls import path
from . import views
from django.contrib import admin
from .views import user_admin_view
from .views import user_admin_view
from .views import ForgotPasswordView, ResetPasswordView, VerifyOTPView

urlpatterns = [
    path('users/', admin.site.urls), 
    path('', views.index, name='index'),
    path('admin/user_admin/', user_admin_view, name='user_admin_view'),
    path('user-admin/', user_admin_view, name='user_admin_view'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('cookie/', views.cookie, name='cookie'),
     path('design/', views.design, name='design'),
    path('demo/', views.request_demo, name='request_demo'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('web_development/', views.web_development, name='web_development'),
    path('school_project/', views.school_project, name='school_project'),
    path('sale_of_accessories/', views.sale_of_accessories, name='sale_of_accessories'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('terms-and-conditions/', views.terms_and_conditions_view, name='terms_and_conditions'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('verify_otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
]


#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)