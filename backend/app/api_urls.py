# -*- coding: utf-8 -*-
from django.urls import path
from .api import (
    FileUploadView,
    CardSearchAPIView,
)

urlpatterns = [
    path('card/upload', FileUploadView.as_view()),
    path('card/search/<str:number>', CardSearchAPIView.as_view()),
]
