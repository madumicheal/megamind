from django.urls import path
from rest_framework.urls import app_name, urlpatterns

from account.api.views import (

    registration_view
)

app_name = "User"

urlpatterns = [
    path('register', registration_view, name="register"),
]