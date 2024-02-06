from django.urls import path
from . import views
app_name='app'
urlpatterns=[
    path('',views.Index,name='index'),
    path('login',views.Login,name='login'),
    path('signup',views.Signup,name='signup'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('cart',views.Cart,name='cart'),
    path('payment',views.Payment,name='payment'),
    path('error/',views.Error,name='error'),
    path('logout/',views.logout,name='logout')
]