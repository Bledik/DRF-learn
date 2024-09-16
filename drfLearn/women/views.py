from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from women.serializers import WomenSerializer

from women.models import Women

# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer 

class  WomenApiView(APIView):
    def get(self, request):
        return Response({'title': "Angelina Jolie"})