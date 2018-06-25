"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from application.views import *
from django.views.decorators.http import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^rest-api/', include('rest_framework.urls')),

    # Rest
    url(r'^mysql/user/$', mysql_user.as_view()),
    url(r'^mysql/user/(?P<id>[0-9]+)/$', mysql_user.as_view()),

    url(r'^redis/user/$', redis_user.as_view()),
    url(r'^redis/user/(?P<id>[-\w]+)/$', redis_user.as_view()),

]