from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def demo(request):
    return render(request, 'index.html')


from django.shortcuts import render

# Create your views here.
