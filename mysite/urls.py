"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    url(r'^$', views.fn_landing_page),  # Landing Page

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # url(r'^login', views.fn_login_page, name='login_page'),
    url(r'^login', auth_views.login, {'template_name': 'login.html'}, name='login'),  # Login Page
    url(r'^auth', views.fn_auth_view),  # Authorization process calls welcome_page if successful login details provided.
    # -------------------------------------------------------
    url(r'^welcome/', views.fn_welcome_page, name='welcome_page'),
    url(r'^sorry/', views.fn_sorry_page, name='sorry_page'),
    url(r'^logout/', views.fn_logout_page, name='logout_page'),
    url(r'^session_expired/', views.fn_session_expired, name='session_expired_page'),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # url(r'^poll/', include('poll.urls')),
    url(r'^poll/', include('poll.urls', namespace="poll"), name='poll_page'),
    # Note: If there are multiple apps, & each app there is a detail.html template file.
    #       So we need to pass 'namespace' argument.
    #       We passing the 'namespace' argument so that the .html files can use it to reference any other .html files in their <a> tags,
    #       so that they can differentiate between which template is being called.
]
