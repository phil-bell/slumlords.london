from django.urls import path
from django.contrib.auth.views import LogoutView

from slumlords.apps.account.views import Login

app_name = "account"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]