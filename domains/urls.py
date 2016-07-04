from django.conf.urls import include, url
from django.contrib import admin
from domains.views import DomainList
from domains.views import DomainCreate

urlpatterns = [
    url(r'^', DomainList.as_view()),
    url(r'^create/', DomainCreate.as_view()),
    url(r'(?P<domain>.*/)'),
]
