from django.urls import path
from . import views

urlpatterns = [
    path('blogpost', views.blog,name="blog"),
    path('', views.showblog,name="showblog"),
    path('blog/api', views.BlogList.as_view(),name="blogApi"),
    path('blog/api/<int:pk>', views.BlogDetail.as_view(),name="singleBlogApi"),
]