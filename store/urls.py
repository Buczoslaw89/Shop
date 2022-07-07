from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.store, name="store"),
    path('home/', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]
