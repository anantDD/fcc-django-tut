"""trydjango_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view
from .views import (
    render_initial_data,
    product_delete_view,
    product_list_view,
    dynamic_lookup_view
)

app_name = "products"
urlpatterns = [
    # path('create/', product_create_view, name='create'),
    path('', product_list_view, name='products'),
    path('list', product_list_view, name='list'),
    path('create/', render_initial_data, name='create'),
    path('<int:my_id>/', dynamic_lookup_view, name='detail'),
    path('<int:my_id>/delete', product_delete_view, name='delete'),
]
