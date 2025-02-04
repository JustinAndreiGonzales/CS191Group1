from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Station
from .serializers import StationSerializer

# Create your views here.
@api_view(['GET'])
def get_all_station(request):
    stations = Station.objects.values('id', 'name', 'is_active')
    return Response(stations)

@api_view(['GET'])
def get_station(request, id):
    station = get_object_or_404(Station, id = id)
    serializer = StationSerializer(station)
    return Response(serializer.data)