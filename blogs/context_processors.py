from blogs.models import Category
from assignment.models import SocialLink

def get_categories(request):
    return {
        'categories': Category.objects.all()
    }

def get_socialLink(request):
    return {
        'socialLink' : SocialLink.objects.all()
    }