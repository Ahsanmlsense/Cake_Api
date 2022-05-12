from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CakesSerializer
from .models import Cakes
# Create your views here.


@api_view(['GET'])
def Home(request):
    """"Function To show the urls for API"""
    urls = {'List of Cakes':"/cakes",
            'Detail of Specified Cake' : "/cake-detail/<id>",
            'Create Cake' : "/addcake",
            'Update Cake' : '/cake-update/<id>',
            'Delete' : 'delete-cake/<id>'
    }
    return Response(urls)

@api_view(['GET'])
def Cakes_Lists(request):
    """
        Function Returns all cakes details
    """
    cakes_objs = Cakes.objects.all()
    serializer_obj = CakesSerializer(cakes_objs,many=True)
    return Response(serializer_obj.data)

@api_view(['GET'])
def Cake_Details(request,pk):
    """ Function Return the detail of the specified cake against Id"""
    try:
        cakes_obj = Cakes.objects.get(id=pk)
        
    except Cakes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer_obj = CakesSerializer(cakes_obj,many=False)
    return Response(serializer_obj.data)

@api_view(['POST'])
def add_cake(request):
    """ Function that add cake details in database"""
    serializer_obj = CakesSerializer(data=request.data)
    if serializer_obj.is_valid():
        serializer_obj.save()
        return Response(serializer_obj.data,status=status.HTTP_201_CREATED)
    return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_cake(request,pk):
    """Update the cake values against the id of cake"""
    try:
        cake_obj = Cakes.objects.get(id=pk)
    except Cakes.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer_obj = CakesSerializer(instance=cake_obj,data=request.data,many=False)
    if serializer_obj.is_valid():
        serializer_obj.save
        return Response(serializer_obj.data,status=status.HTTP_201_CREATED)
    return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["DELETE"])
def delete_cake(request,pk):
    """Delete the specified cake against id"""
    try:
        cake_obj = Cakes.objects.get(id=pk)
        
    except Cakes.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    cake_obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    