from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['-updated_at']

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    STATUS_CHOICES = (
        ("Draft","Draft"),
        ("Published","Published")
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,unique=True,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='blogs')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=25,choices=STATUS_CHOICES , default= "Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.pk:
            old = Blog.objects.get(pk=self.pk)
            title_changed = old.title != self.title
        else:
            title_changed = True

        if title_changed:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Blog.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)
