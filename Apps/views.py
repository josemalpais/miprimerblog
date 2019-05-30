from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def Apps(request):
	posts=Post.objects.all().order_by('created_date')
	return render(request, 'Apps/post_list.html', {'posts':posts})

