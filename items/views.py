from django.views.generic.base import TemplateView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import ItemInstance, ItemTag, ItemTagValue
from rest_framework import viewsets


class ItemInstanceViewSet(viewsets.ModelViewSet):
    model = ItemInstance


class ItemInstanceCreateReadView(ListCreateAPIView):
    model = ItemInstance


class ItemInstanceReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    model = ItemInstance


class ItemTagViewSet(viewsets.ModelViewSet):
    model = ItemTag


class ItemTagValueViewSet(viewsets.ModelViewSet):
    model = ItemTagValue


class HomePage(TemplateView):
    template_name = "home.html"