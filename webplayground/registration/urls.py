from django.urls import path
from .views import SinUpView, ProfileUpdate

urlpatterns = [
    path("signup/", SinUpView.as_view(), name="signup"),
    path("profile/", ProfileUpdate.as_view(), name="profile"),
]
