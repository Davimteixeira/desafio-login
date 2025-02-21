from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import CustomLoginView  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("", CustomLoginView.as_view(), name="home"), 
]
