from django.contrib import admin
from blogs.models import Category , Blog
# Register your models here.


admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','author', 'status', 'is_featured', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'is_featured', 'created_at', 'author')
    search_fields = ('id','title','category__name')