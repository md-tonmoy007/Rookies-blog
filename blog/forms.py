from django.forms import ModelForm
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class PostForm(ModelForm):
	class Meta:
		model = Post 
		fields = '__all__'



# class CreateUserForm(UserCreationForm):
# 	class Meta(object):
# 		model = User 
# 		fields = ['username', 'email', 'password1', 'password2']
