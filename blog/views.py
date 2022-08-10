from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Blog
from.serializer import BlogSerializer
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['id','title','status']
    search_fields =['id','title','status']
    ordering_fields=['id','title','status']
    



class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

def showblog(request):
     blogs= Blog.newmanager.all()

     context ={
        'blogs':blogs
    }
     return render(request, 'blog_home.html',context)

def blog(request):
    if request.method =='POST':
        title= request.POST.get('title')
        desc= request.POST.get('desc')
        img= request.FILES.get('myimage')

        newitem = Blog(title=title,desc=desc,img=img)
        newitem.save()
        messages.info(request,"Your post has been saved successfully!")
        return redirect('blog')

    else:
        return render(request,'blog.html')

