from django.conf.urls import patterns, include, url



from .models import UserList, UserDetail
from .models import AllLists, ListDetail
from .models import ItemList, ItemDetail, ListItemList

user_urls = patterns('',
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/lists', UserList.as_view(), name='user-lists'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
)

list_urls = patterns('',
    url(r'^/(?P<pk>\d+)/items', ListItemList.as_view(), name='item-list'),
    url(r'^/(?P<pk>\d+)$', ListDetail.as_view(), name='list-detail'),
    url(r'^$', AllLists.as_view(), name='all-lists')
)

item_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', ItemDetail.as_view(), name='item-detail'),
    url(r'^$', ItemList.as_view(), name='item-list')
)

urlpatterns = patterns('',
    url(r'^users', include(user_urls)),
    url(r'^lists', include(list_urls)),
    url(r'^items', include(item_urls)),
)
