from rest_framework import generics, permissions

from .serializers import UserSerializer, ListSerializer, ItemSerializer
from .models import User, List, Item


class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'username'


class AllLists(generics.ListCreateAPIView):
    model = List
    serializer_class = ListSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    model = List
    serializer_class = ListSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserLists(generics.ListAPIView):
    model = List
    serializer_class = ListSerializer

    def get_queryset(self):
        queryset = super(UserLists, self).get_queryset()
        return queryset.filter(creator__username=self.kwargs.get('username'))


class ItemList(generics.ListCreateAPIView):
    model = Item
    serializer_class = ItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Item
    serializer_class = ItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ListItemList(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super(ListItemList, self).get_queryset()
        return queryset.filter(list__pk=self.kwargs.get('pk'))
