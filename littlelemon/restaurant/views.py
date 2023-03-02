from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer
from .models import menu, Booking
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def sayhello(request):
    return HttpResponse('Hello')

def index(request):
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes =[IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]