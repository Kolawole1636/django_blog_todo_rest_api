from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from todo import serializers

# Create your views here.

@api_view(['GET','POST'])
def todoApi(request):
    if request.method=='GET':
        item = Todo.objects.all()
        serializer = TodoSerializer(item, many =True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def todoApiSingle(request,pk):

    try:
        item = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = TodoSerializer(item)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = TodoSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        item.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)









def todolist(request):
    todos = Todo.objects.all()
    context={'todos':todos}
    return render(request,'todo.html',context)


def createtodo(request):
    if request.method=='POST':
        title=request.POST["todo"]
        todoitem =Todo(title=title)
        todoitem.save()
        return redirect('todolist')
    

def updatetodo(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method=='POST':
        title=request.POST['todo']
        todo.title=title
        todo.save()
        return redirect('todolist')
    
    
    return render(request,'updatetodo.html',{'todo':todo})


def deletetodo(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todolist')






