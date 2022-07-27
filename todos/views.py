from django.shortcuts import render
from todos.serializer import TodoSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from todos.models import Todo 
import requests
from corsheaders.defaults import default_headers

# Create your views here.
@api_view(['POST'])
def createtodo(request):
    record=TodoSerializer(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)


@api_view(['GET'])
def alltodos(request):
    record= Todo.objects.all()
    info = TodoSerializer(record, many=True)
    return Response(info.data)


@api_view(['DELETE'])
def deletetodo(request, id):
    record= Todo.objects.get(id=id)
    record.delete()
    return Response('Todo successfully deleted')


@api_view(['GET'])
def tododetails(request, id):
    record= Todo.objects.get(id=id)
    info= TodoSerializer(record,many=False)
    return Response(info.data)


@api_view(['PUT'])
def todoedit(request, id):
    record=Todo.objects.get(id=id)
    info=TodoSerializer(data=request.data, instance=record)
    if info.is_valid():
        info.save()
        return Response('Updated successfully')
    

def about(request):
    url= requests.get('http://localhost:8000/api/v1/alltodos')
    data = url.json()
    context = {'data': data}
    return render(request, 'api/about.html', context)

