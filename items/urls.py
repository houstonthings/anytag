# from django.conf.urls import patterns, url
# from lists import views
#
# urlpatterns = patterns('',
#     url(
#         regex=r"^$",
#         view=views.ListParentItemCreateReadView,
#         name="list_rest_api"
#     ),
#     url(
#         regex=r"^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/$",
#         view=views.ListParentReadUpdateDeleteView,
#         name="list_rest_api"
#     ),
# )