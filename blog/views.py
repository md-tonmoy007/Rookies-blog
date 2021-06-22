

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from blog.models import *
from blog.forms import *


def Bloglist(request):
	queryset = Post.objects.filter(status=1).order_by('-created_on')[:8]
	context = {'publish_posts':queryset}
	return render(request,'blog/home.html',context)


def BlogDetails(request,slug):
	post = Post.objects.get(slug=slug)
	context = {'post':post}
	return render(request,'blog/details.html', context)

def about(request):
	return render(request, 'blog/about.html')


def search(request):
	if request.method == 'GET':
		search = request.GET.get('search')
		titles = Post.objects.filter(title__contains = search)
		contents = Post.objects.filter(content__contains = search)


	context = {'titles':titles, 'contents':contents}
	return render(request, 'blog/search.html',context)



def FullBlogList(request):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	categories = Concept.objects.all()
	context = {'all_posts':queryset, 'categories':categories}
	return render(request,'blog/bloglist.html',context)



def Categorical(request, pk):
	posts = Post.objects.filter(category=pk)
	categories= Concept.objects.all()

	context = {'posts':posts, 'categories':categories}
	return render(request, 'blog/category.html', context)


def Header(request):
	categories = Concept.objects.all()
	context={'categories':categories}
	return render(request, 'blog/catmbl.html', context)




def CreatePost(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('bloglist')

	context = {'form':form}
	return render(request, 'blog/post_form.html', context)


