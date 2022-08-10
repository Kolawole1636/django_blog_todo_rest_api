from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login(request):
    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, 'blog.html')
           # return redirect("blog")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")


    else:
        return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        email =   request.POST.get('email')

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username has already been used!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"email has already been used!")
                 return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,email=email)
                user.save()
                messages.info(request,"you have been registered successfully")
                return redirect("login")

        else:
            messages.info(request,"passwords are not matching")
            return redirect('register')
     

    else: 
        return render(request, 'register.html')



def logout(request):
    auth.logout(request)
    return redirect("login")