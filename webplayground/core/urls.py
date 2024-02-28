from django.urls import path, include
from .views import HomePageView, SamplePageView
from pages.urls import pages_patterns


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("pages/", include(pages_patterns)),
    path("sample/", SamplePageView.as_view(), name="sample"),
]
