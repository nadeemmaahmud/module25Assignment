from django.shortcuts import render
from .models import Contents

def home(request):
    posts = Contents.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})