from django.urls import path
from .views import SinUpView, ProfileUpdate, EmailUpdate

urlpatterns = [
    path("signup/", SinUpView.as_view(), name="signup"),
    path("profile/", ProfileUpdate.as_view(), name="profile"),
    path("profile/email/", EmailUpdate.as_view(), name="profile_email"),
]
