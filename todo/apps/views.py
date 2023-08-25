from django.shortcuts import render,get_object_or_404
from .models import Todo #Todo is model database
from .serializers import TodoSerializer #serializer of todo list it contain three fields
from rest_framework.response import Response #rest framework drf response 
from rest_framework.decorators import api_view #api decorator display a view and using these method only
from rest_framework import status #it will helps to display http status code

# Create your views here.
@api_view(['GET','POST'])
def todo_list(request):
    if request.method=="GET":
        todos=Todo.objects.all()
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PATCH","PUT","DELETE"])
def todo_details(request,pk):
    todo=get_object_or_404(Todo,id=pk)
    if request.method=="GET":
        serializer=TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=TodoSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
