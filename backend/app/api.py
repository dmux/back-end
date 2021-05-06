# -*- coding: utf-8 -*-
import uuid
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .utils import parser
from .models import CardRow
from .serializers import CardRowSerializer


class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        upload = request.FILES['post']
        file_object = upload.read().decode('utf-8')
        filepath = '/tmp/{}.txt'.format(uuid.uuid4())
        f = open(filepath, 'w')
        f.write(file_object)
        f.close()
        parser(filepath)

        return Response(status=status.HTTP_200_OK)


class CardSearchAPIView(ListAPIView):
    serializer_class = CardRowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CardRow.objects.all()
        number = self.request.query_params.get('number')
        if number is not None:
            queryset = queryset.filter(number__exact=number)
        return queryset
