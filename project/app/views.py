from django.shortcuts import render
from .models import Detail


# Create your views here.
def accept(request):
    return render(request,'app/base.html')
