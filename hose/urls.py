from django.contrib import admin
from django.urls import path
from . import views
from .views import CreateProperty, PropertyByUser

app_name = 'hose'

urlpatterns = [
    path('', views.index, name='home'),
    path('single-list/', views.single_list, name='single-list'),
    path('single-blog/<int:b_id>', views.single_blog, name='single-blog'),
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
    path('messages/', views.msg, name='messages'),
    path('bookings/', views.bookings, name='bookings'),
    path('invoices/', views.invoices, name='invoice'),
    path('create-property/', CreateProperty.as_view(), name='create'),
    path('user-property/', PropertyByUser.as_view(), name='user-property'),
    path('logout/', views.logoutuser, name='logout'),
    path('testing/', views.add_property, name='test'),
   
]
