from django.urls import path
from .views import CustomLoginView, CustomRegisterView, CustomLogoutView, MenuView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("menu/", MenuView.as_view(), name="menu"),
]
