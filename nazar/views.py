from django.shortcuts import render

# Create your views here.
def subscribe(request):
    context={}
    return render(request,'nazar/subscribe.html', context)
