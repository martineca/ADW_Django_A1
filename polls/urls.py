from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
     # setting up the route page
     # page that will load when the site is loaded
    path('', views.IndexView.as_view(), name='index'),

]