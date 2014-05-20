from django.conf.urls import patterns, include, url

from django.contrib import admin
from items.views import ItemInstanceViewSet, HomePage, ItemTagViewSet, ItemTagValueViewSet
from rest_framework import routers

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'items', ItemInstanceViewSet)
router.register(r'tags', ItemTagViewSet)
router.register(r'tagvalues', ItemTagValueViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^items/', HomePage.as_view()),
    url(r'^', include('lists.urls')),
    #url(r'^$', lists.urls, name='home'),
)


from django.conf import settings
from django.conf.urls import include, patterns, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )