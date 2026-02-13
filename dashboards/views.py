from django.shortcuts import render , redirect , get_object_or_404
from blogs.models import Category , Blog
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, user_passes_test
from dashboards.forms import CategoryForm , BlogPostForm , AddUserForm , EditUserForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def unified_403_404_view(request, exception=None):
    return render(request, 'forbidden_or_notfound.html', status=404)

def is_manager_or_editor(user):
    if user.is_superuser:
        return True
    return user.groups.filter(name__in=['Manager', 'Editor']).exists()


def is_manager(user):
    if user.is_superuser:
        return True
    return user.groups.filter(name__in=['Manager']).exists()


@user_passes_test(is_manager_or_editor)
def dashboard(request):
    category_count = Category.objects.count()
    blogs_count = Blog.objects.count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count
    }
    return render(request, 'dashboard/dashboard.html', context)



@user_passes_test(is_manager_or_editor)
def categories(request):
    return render(request , 'dashboard/categories.html')

@user_passes_test(is_manager_or_editor)
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")
            return redirect('categories')
    context = {
        'form' : form
    }
    return render(request , 'dashboard/add_category.html' , context)

@user_passes_test(is_manager_or_editor)
def edit_category(request , pk):
    category = get_object_or_404(Category , pk = pk)
    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST , instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    context = {
        'form' : form,
        'category' : category
    }
    return render(request , 'dashboard/edit_category.html' , context)

@user_passes_test(is_manager_or_editor)
def delete_category(request , pk):
    category = get_object_or_404(Category , pk = pk)
    category.delete()
    return redirect('categories')

@user_passes_test(is_manager_or_editor)
def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts' : posts
    }
    return render(request , 'dashboard/post.html' , context)

@user_passes_test(is_manager_or_editor)
def add_post(request):
    form = BlogPostForm()
    if request.method == "POST":
        form = BlogPostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    context = {
        'form' : form
    }
    return render(request , 'dashboard/add_post.html',context)

@user_passes_test(is_manager_or_editor)
def edit_post(request , pk):
    post = get_object_or_404(Blog , pk = pk)
    form = BlogPostForm(instance=post)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {
        'form' : form,
        'post' : post
    }
    return render(request , 'dashboard/edit_post.html',context)

@user_passes_test(is_manager_or_editor)
def delete_post(request , pk):
    post = get_object_or_404(Blog , pk = pk)
    post.delete()
    return redirect('posts')


@user_passes_test(is_manager)
def users(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request , 'dashboard/users.html' , context)

@user_passes_test(is_manager)
def add_user(request):
    form = AddUserForm()
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    context = {
        'form' :form
    }
    return render(request , 'dashboard/add_user.html' , context)

@user_passes_test(is_manager, login_url='login')
def edit_user(request , pk):
    user = get_object_or_404(User , pk = pk)
    form = EditUserForm(instance=user)
    if request.method == "POST":
        form = EditUserForm(request.POST ,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {
        'form' : form,
        'user' : user
    }
    return render(request ,'dashboard/edit_user.html' , context)

def delete_user(request , pk):
    user = get_object_or_404(User , pk = pk)
    user.delete()
    return redirect('users')
