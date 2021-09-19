from rest_framework import permissions, serializers, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import HomeDetailsSerializer, HomeSerializer, ImageFilesSerializer
from .models import ImageFiles, Home
# Create your views here.


class HomeListView(ListAPIView):
    serializer_class = HomeSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'


class HomeDetailsView(RetrieveAPIView):
    serializer_class = HomeSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'


class ImageView(APIView):
    def get(self, request, pk, format=None):
        home = Home.objects.get(pk=pk)
        images = home.images.all()
        serializer = ImageFilesSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
