from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path(
        "login/", auth_view.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="index.html"),
        name="logout",
    ),
    path("profile/", views.profile, name="profile"),
    path("account/update/", views.changeAccount, name="updateAccount"),
]
