from django.shortcuts import render

# Create your views here.

def Apps(request):
	return render(request, 'Apps/post_list.html', {})
