from pickletools import float8, int4
from django.http import HttpResponse
from django.shortcuts import render
import math

# Create your views here.

def calculator(request):
    return render(request,'calculator.html')

def add(request):
    
    if request.method=="POST":
        try:

            val1 = float(request.POST['val1'])
            val2 = float(request.POST['val2'])
            opr = request.POST["opr"]

            if opr=="+":
                result = val1 + val2
            elif opr=="-":
                result = val1 - val2
            elif opr=="x":
                result = val1 * val2
            elif opr=="/":
                result = val1/val2
            elif opr=="pow":
                result = val1 ** val2
            elif opr=="sqrt":
                result = math.sqrt(val1)
        except:
            result="Invalid"


    myresult = {"result":result }

    return render(request,"calculator.html",myresult)












