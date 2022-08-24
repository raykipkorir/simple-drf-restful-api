from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from app.models import Drink
from .serializers import DrinkSerializer


@api_view(["GET", "POST"])
def drink_list(request, format=None):

    instance = get_list_or_404(Drink)

    if request.method == "GET":
        serializer = DrinkSerializer(instance=instance, many=True)
        return Response({"drinks":serializer.data}, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(["GET", "PUT", "DELETE"])
def drink_detail(request, pk=None, format=None):

    instance = get_object_or_404(Drink, pk=pk)

    if request.method == "GET":
        serializer = DrinkSerializer(instance=instance)
        return Response({"drinks":serializer.data}, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = DrinkSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        
    if request.method == "DELETE":
        instance.delete()
        return Response("Deleted", status=status.HTTP_204_NO_CONTENT)
