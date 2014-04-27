from django.conf.urls import patterns, include, url

from django.contrib import admin
from items.views import ItemTypeViewSet, ItemInstanceViewSet
from rest_framework import routers

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'items', ItemInstanceViewSet)
router.register(r'types', ItemTypeViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('lists.urls')),
    #url(r'^$', lists.urls, name='home'),
)
