from django.urls import path, include
from .views import HomePageView, SamplePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("pages/", include("pages.urls"), name="home"),
    path("sample/", SamplePageView.as_view(), name="sample"),
]
