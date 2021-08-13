from django.contrib import admin
from django.urls import path
from . import views
from .views import CreateProperty, PropertyByUser, UpdateProperty, DeleteProperty
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.forms import  PasswordResetForm


app_name = 'hose'

urlpatterns = [
    path('', views.index, name='home'),
    path('single-list/', views.single_list, name='single-list'),
    path('single-blog/<int:b_id>/', views.single_blog, name='single-blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('categories/', views.categories, name='cat'),
    path('blog/', views.blog, name='blog'),
    path('register/', views.register, name='register'),
    path('logiin/', views.logiin, name='logiin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.my_profile, name='my-profile'),
    path('favourite/', views.favorite, name='favourite'),
    path('submitprop/', views.submit_property, name='submit-property'),
    path('messages/', views.messages, name='messages'),
    path('bookings/', views.bookings, name='bookings'),
    path('invoices/', views.invoices, name='invoice'),
    path('create-property/', CreateProperty.as_view(), name='create'),
    path('edit-post/<int:pk>/', UpdateProperty.as_view(), name='edit_post'),
    path('delete-property/<int:pk>/', DeleteProperty.as_view(), name='delete_post'),
    path('user-property/', PropertyByUser.as_view(), name='user-property'),
    path('logout/', views.logoutuser, name='logout'),
    path('testing/', views.add_property, name='test'),
    path ('prop/', views.about, name='property-user'),
    path(
        'reset-password/',
        auth_views.PasswordResetView.as_view(template_name='hose/reset-password.html', 
        email_template_name='hose/-reset-email.html', 
        success_url = reverse_lazy('hose:password_reset_done'), form_class= PasswordResetForm), name='password_reset'
     ),

    path(
       'password-reset-done/',
       auth_views.PasswordResetDoneView.as_view(template_name='hose/password-reset-done.html'),
       name='password_reset_done'
    ),

    path(
       'password-reset/<uidb64>/<token>/',
       auth_views.PasswordResetConfirmView.as_view(template_name='hose/password-confirm-form.html',
       form_class=SetPassword, success_url = reverse_lazy('hose:password_reset_complete')), name='password_reset_confirm'
    ),
     path(
       'password-reset-complete/',
       auth_views.PasswordResetCompleteView.as_view(template_name='hose/password-reset-complete.html'), 
       name='password_reset_complete'
    ),
    ]
