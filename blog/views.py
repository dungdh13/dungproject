from django.shortcuts import render
from .models import Post



def home(request):
	content = {
		'posts': Post.objects.all().order_by('-id')
	}
	return render(request, 'blog/home.html',content)

def about(request):
	return render(request, 'blog/about.html',{'title': 'About'})