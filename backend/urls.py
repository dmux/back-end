# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import (
    include,
    path,
)

admin.site.site_header = 'Backend - Desafio Hyperativa'

urlpatterns = [
    path('api/', include('backend.api.urls'), name='api'),
    path('admin', admin.site.urls),
]
