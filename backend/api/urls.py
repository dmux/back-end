# -*- coding: utf-8 -*-
from django.urls import (
    include,
    path,
)
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'

schema_view = get_schema_view(openapi.Info(
    title='Backend - Desafio Hyperativa / APIs',
    default_version='v1',
    description='Todas as APIs foram desenvolvidas baseadas na tecnologia REST, \
            seguindo os atuais padrões técnicos de mercado. \
            Procure na documentação informações de como consumir essas APIs.',
    terms_of_service='',
    contact=openapi.Contact(email='rafael.sales@gmail.com')),
                              public=True,
                              permission_classes=(AllowAny, ))

urlpatterns = [
    path('',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='swagger-ui'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('app/', include('backend.app.api_urls'), name='app'),
]
