from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .serializers import MenuItemSerializer, BookingItemSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

"""
@api_view(["POST","GET"])
def test(request):
    return Response("test end point", status=status.HTTP_200_OK)

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_delivery(user):
    return user.groups.filter(name='Delivery crew').exists()

def is_customer(user):
    #Need to implement properly
    return True

class BookingItemView(APIView):
    def get(self, request):
        queryset = Booking.objects.all()
        serializer = BookingItemSerializer(queryset, many=True)
        return Response({'Bookings': serializer.data}, status=status.HTTP_200_OK)

class SingleMenuItemView(APIView):
    def get(self, request):
        queryset = Menu.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response({'MenuItems': serializer.data}, status=status.HTTP_200_OK)

class MenuItemView(APIView):
    def get(self, request):
        queryset = Menu.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response({'MenuItems': serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = MenuItemSerializer(data=request.POST.dict())
        if(serializer.is_valid()):
            serializer.save()
            return Response({'Message': "Successfully added"}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({'Message': "Data validation error " + str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request):
        return Response({'Message': "Access denied"}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request):
        return Response({'Message': "Access denied"}, status=status.HTTP_403_FORBIDDEN)
    def put(self, request):
        return Response({'Message': "Access denied"}, status=status.HTTP_403_FORBIDDEN)
"""

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingItemSerializer
    permission_classes = [IsAuthenticated]