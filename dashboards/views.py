from django.shortcuts import render , redirect , get_object_or_404
from blogs.models import Category , Blog
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, user_passes_test
from dashboards.forms import CategoryForm
from django.contrib import messages
# Create your views here.

def unified_403_404_view(request, exception=None):
    return render(request, 'forbidden_or_notfound.html', status=404)

def is_manager_or_editor(user):
    return user.groups.filter(name__in=['Manager','Editor']).exists()


# @login_required(login_url = None)
@user_passes_test(is_manager_or_editor)
def dashboard(request):
    if not request.user.is_authenticated:
        # logged-out user
        raise PermissionDenied
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'category_count' : category_count,
        'blogs_count' : blogs_count
    }

    return render(request , 'dashboard/dashboard.html' , context)

@login_required(login_url = 'login')
@user_passes_test(is_manager_or_editor)
def categories(request):
    return render(request , 'dashboard/categories.html')


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


def delete_category(request , pk):
    category = get_object_or_404(Category , pk = pk)
    category.delete()
    return redirect('categories')
