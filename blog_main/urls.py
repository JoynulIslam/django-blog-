
from django.contrib import admin
from django.urls import path,include
from .views import home,register,login,logout
from django.conf.urls.static import static
from django.conf import settings
from blogs.views import blogs,search

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home,name='home'),
    path('category/',include('blogs.urls')),
    path('blogs/<slug:slug>/',blogs,name='blogs'),
    #search endpoint
    path('blogs/search/',search,name='search'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
