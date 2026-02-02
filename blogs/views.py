from django.http import HttpResponse
from django.shortcuts import render,redirect , get_object_or_404
from blogs.models import Category , Blog
from django.db.models import Q
# Create your views here.

def post_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published',category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    # category = get_list_or_404(Category , pk = category_id)
    context = {
        'posts' : posts,
        'category' : category
    }
    return render(request , 'post_by_category.html',context) 

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    return render(request, 'blog.html', {
        'single_blog': single_blog
    })


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status='Published')
    context = {
        'blogs' : blogs,
        'keyword' : keyword
    }
    return render(request,'search.html',context)