from django.conf.urls import patterns, url

urlpatterns = patterns('lists.views',
    url(r'^$', 'home'),
    #url(r'^(?P<user_name>[\w\s\d]+)/$', 'view_list', {'list_name': 'inbox'}),
    url(r'^(?P<user_name>[\w\s\d]+)/add/(?P<new_item>.+)$', 'add_item', {'list_name': 'inbox'}),
    url(r'^(?P<user_name>[\w\s\d]+)/move/(?P<pk>[\w\s\d]+)/$', 'move_item'),
    url(r'^(?P<user_name>[\w\s\d]+)/update/(?P<pk>[\w\s\d]+)/$', 'update_item', {'list_name': 'inbox'}),
    url(r'^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/move/(?P<pk>[\w\s\d]+)/$', 'move_item'),
    url(r'^(?P<user_name>[\w\s\d]+)/remove/(?P<pk>[\w\s\d]+)/$', 'remove_item', {'list_name': 'inbox'}),
    url(r'^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/$', 'view_list'),
    url(r'^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/add/(?P<new_item>.+)$', 'add_item'),
    url(r'^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/remove/(?P<pk>[\w\s\d]+)$', 'remove_item'),
    url(r'^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/update/(?P<pk>[\w\s\d]+)/$', 'update_item'),
    url(r'^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/clear/$', 'clear_list'),
)
