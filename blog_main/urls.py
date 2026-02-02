
from django.contrib import admin
from django.urls import path,include
from .views import home
from django.conf.urls.static import static
from django.conf import settings
from blogs.views import blogs,search

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home,name='home'),
    path('category/',include('blogs.urls')),
    path('<slug:slug>/',blogs,name='blogs'),
    #search endpoint
    path('blogs/search/',search,name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
