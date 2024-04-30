from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from GeoAPIs.models import TypeProducer, UserProducer
from GeoAPIs.serializers import TypeProducerSerializer, UserProducerSerializer

# Vistas para TypeProducers

@csrf_exempt
@api_view(['GET', 'POST'])
def type_producer_list(request):
    if request.method == 'GET':
        producers = TypeProducer.objects.all()
        serializer = TypeProducerSerializer(producers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = TypeProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def type_producer_detail(request, pk):
    try:
        producer = TypeProducer.objects.get(pk=pk)
    except TypeProducer.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = TypeProducerSerializer(producer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = TypeProducerSerializer(producer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        producer.delete()
        return JsonResponse(status=204)
    
    
# Vistas para UserProducers

@csrf_exempt
@api_view(['GET', 'POST'])
def user_producer_list(request):
    if request.method == 'GET':
        producers = UserProducer.objects.all()
        serializer = UserProducerSerializer(producers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def user_producer_detail(request, pk):
    try:
        producer = UserProducer.objects.get(pk=pk)
    except UserProducer.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = UserProducerSerializer(producer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProducerSerializer(producer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        producer.delete()
        return JsonResponse(status=204)