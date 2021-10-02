from django.contrib.admin.sites import site
from django.db.models.deletion import RESTRICT
from django.shortcuts import render
from django.template.response import ContentNotRenderedError
from .models import NavbarModel, Settings, Footer, MiniNavbarModel, Category, Sub_Category, ProductModel
# Create your views here.

def home_view(request):
    context = {}
    navbar_queryset = NavbarModel.objects.all()
    settings_queryset =  Settings.objects.all()
    footer_queryset = Footer.objects.all()
    # mininavbar_queryset = MiniNavbarModel.objects.all()
    # redcard_queryset = RedCard.objects.all()
    product_queryset = ProductModel.objects.all()

    context['navbar_queryset '] = navbar_queryset
    context['settings_queryset'] = settings_queryset
    context['footer_queryset'] = footer_queryset
    context['product_queryset'] = product_queryset


    return render(request, 'index.html', context)