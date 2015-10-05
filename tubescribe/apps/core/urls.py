from django.conf.urls import include, url
from django.contrib import admin

try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *


from tubescribe.apps.core import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tubescribe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^', ),

    url(r'^$', views.index, name='index'),
    url(r'^get_video$', views.AjaxView, name='get_video'),
    url(r'^test/', views.test, name='test'),
    url(r'^test_get_video$', views.test, name='test_get_video'),
    url(r'^create_post/',views.create_post),
    url(r'^console/',views.my_view),
]
