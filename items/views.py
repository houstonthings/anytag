from django.views.generic.base import TemplateView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import ItemInstance, ItemType
from rest_framework import viewsets


class ItemInstanceViewSet(viewsets.ModelViewSet):
    model = ItemInstance


class ItemTypeViewSet(viewsets.ModelViewSet):
    model = ItemType


class ItemInstanceCreateReadView(ListCreateAPIView):
    model = ItemInstance


class ItemInstanceReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    model = ItemInstance


class HomePage(TemplateView):
    template_name = "home.html"