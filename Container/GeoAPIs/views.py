from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from GeoAPIs.models import TypeProducer, UserProducer
from GeoAPIs.serializers import TypeProducerSerializers, UserProducerSerializers

# Vistas para TypeProducers

@csrf_exempt
@api_view(['GET', 'POST'])
def type_producer_list(request):
    if request.method == 'GET':
        producers = TypeProducer.objects.all()
        serializer = TypeProducerSerializers(producers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # type_producer_data = JSONParser().parse(request)
        serializer = TypeProducerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def type_producer_detail(request, pk):
#     try:
#         producer = TypeProducer.objects.get(pk=pk)
#     except TypeProducer.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = TypeProducerSerializers(producer)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TypeProducerSerializers(producer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         producer.delete()
#         return Response(status=204)
    
    
# # Vistas para UserProducers

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def user_producer_list(request):
#     if request.method == 'GET':
#         producers = UserProducer.objects.all()
#         serializer = UserProducerSerializers(producers, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = UserProducerSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_producer_detail(request, pk):
#     try:
#         producer = UserProducer.objects.get(pk=pk)
#     except UserProducer.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = UserProducerSerializers(producer)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = UserProducerSerializers(producer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         producer.delete()
#         return Response(status=204)