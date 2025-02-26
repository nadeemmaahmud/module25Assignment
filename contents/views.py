from django.shortcuts import render, redirect
from .models import Contents
from . forms import CreatePostForm
from django.contrib import messages

def home(request):
    posts = Contents.objects.all().order_by('-created_at')
    return render(request, 'contents/home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post created successfully')
            return redirect('home')
    else:
        form = CreatePostForm()

    return render(request, 'contents/create_edit_post.html', {'form': form, 'create': True})