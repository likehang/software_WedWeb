"""weddingWeb URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import logout
from django.conf import settings
from Web.api import *
from Web.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',index),
    url(r'^login/$', index_login),
    url(r'^register/$', index_register),
    url(r'^logout/$', logout, {'next_page': '/register'}),
    url(r'^backManage/$',backWeb),
    url(r'^single/(?P<id>\d+)$',single),
    url(r'^gallery/$',gallery),
    url(r'^person/$',person),
    url(r'^person-fav/$',person_fav),
    url(r'^person-list/$',person_list),
    url(r'^server/(?P<site>\d+)&(?P<kind>\d+)$',server),

    url(r'api/getCServer/$',getCServer),
    url(r'api/getServer_kind/$',getServer_kind),
    url(r'api/getCity/$',getCity),
    url(r'api/getBusinessKind/$',getBusinessKind),

    url(r'api/getserver_graphs/$',getserver_graphs),
    url(r'api/manageCompany/$',manageCompany),
    url(r'api/getClist/$',getClist),
    url(r'api/manageOrderList/$',manageOrderList),
    url(r'api/manageFav/$',manageFav),
    
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)