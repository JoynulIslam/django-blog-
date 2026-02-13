from django import forms
from blogs.models import Category , Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'})
        }

        

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','category','featured_image','short_description','blog_body','status','is_featured']


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions','password1','password2']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions']
