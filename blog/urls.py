from django.urls import path
from blog import views

urlpatterns = [
	
	path('', views.Bloglist, name='home'),
	path('post_detail/<slug:slug>/', views.BlogDetails, name='blog_details'),
	path('about/', views.about, name='about'),
	path('search/', views.search, name='search'),
	path('bloglist/', views.FullBlogList, name='bloglist'),
	path('category/<int:pk>/', views.Categorical, name='category' ),
	path('catmbl/', views.Header, name= 'catmbl'),
	path('post_admin/', views.CreatePost, name='createpost'),
]