from craiglist_clone import urls
from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('new-search/', views.new_search, name="new_search"),
    ]