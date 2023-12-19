from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':10, 'b':100}
    return render(request,'h1.html',context=d)