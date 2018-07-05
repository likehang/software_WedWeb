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
    url(r'^logout/$', logout, {'next_page': '/index'}),
    url(r'^backManage/$',backWeb),
    url(r'^single/(?P<id>\d+)$',single),
    url(r'^single/(?P<ser_id>\d+)/(?P<msg>\w+)/(?P<way>\w+)$',favfunction),
    url(r'^company/(?P<id>\d+)$',company),
    url(r'^person/',person),
    url(r'^person-fav/',person_fav),
    url(r'^person-list/',person_list),
    url(r'^server/(?P<site>\d+)&(?P<kind>\d+)$',server),

    url(r'api/getCServer/$',getCServer),
    url(r'api/ManageCServer/(?P<id>\d+)$',ManageCServer),
    url(r'api/getServer_kind/$',getServer_kind),
    url(r'api/getCity/$',getCity),
    url(r'api/getBusinessKind/$',getBusinessKind),
    

    url(r'api/getserver_graphs/(?P<id>\d+)$',getserver_graphs),
    url(r'api/manageCompany/$',manageCompany),
    url(r'api/getputClist/$',getputClist),
    url(r'api/manageOrderList/(?P<id>\d+)/(?P<msg>\w+)$',manageOrderList),
    url(r'api/getFav/$',getFav),
    url(r'api/dpFav/(?P<ser_id>\d+)$',dpFav),
    

    url(r'api/searchServer/(?P<msg>\w+)$',searchS),
    url(r'api/searchCompany/(?P<msg>\w+)$',searchCom),
    url(r'api/searchCity/(?P<msg>\w+)$',searchCity),



    
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)