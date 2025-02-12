from django.urls import path
from .views import home

app_name = 'sitevisitor'
urlpatterns = [
    path('', home, name='home'),
]