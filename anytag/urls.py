from django.conf.urls import patterns, include, url

from django.contrib import admin
import listapi
import lists

admin.autodiscover()

urlpatterns = patterns('',
   url(r'^', include('lists.urls')),

    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api/', include(listapi.urls, namespace='list_api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lists.urls, name='home'),
)
