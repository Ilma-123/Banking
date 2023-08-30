from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),

    path('credentials/register/', views.register, name='register'),
    path('credentials/redirect_register/', views.redirect_register, name='redirect_register'),

    path('logout/', views.logout_view, name='logout'),
    path('register-customer/', views.register_customer, name='register_customer'),
    path('newpage/', views.newpage, name='newpage'),
    path('fetch-branches', views.fetch_branches, name='fetch_branches'),

    path('show_form/', views.show_form, name='show_form'),




]









