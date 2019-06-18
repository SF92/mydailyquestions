from django.conf.urls import url
from user_management import views
from django.conf.urls import url, include

# TEMPLATE TAGGING
app_name = "user_management"

urlpatterns = [
    url("UserLogin/", views.UserLogin.as_view(), name="UserLogin"),
    url("UserSignUp/", views.UserSignUp.as_view(), name="UserSignUp"),
]

