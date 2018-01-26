"""notesOrganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from polls import views as core_views


#route configuration for main page(notes) and admin page
urlpatterns = [
    path('', include('polls.urls')),
    url(r'^$', core_views.IndexView.as_view(), name='note_list'),
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^new$', core_views.NoteCreate.as_view(), name='note_new'),
    url(r'^edit/(?P<pk>\d+)$', core_views.NoteUpdate.as_view(), name='note_edit'),
    url(r'^delete/(?P<pk>\d+)$', core_views.NoteDelete.as_view(), name='note_delete'),
]