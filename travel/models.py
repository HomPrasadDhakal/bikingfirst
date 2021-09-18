from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

# MODELS FOR CATEGORY SUB CATEGORY & ALL CATEGORY

#MODELS FOR CATEGORY
class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title
    
#MODELS FOR SUB CATEGORY
class SubCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title


#MODELS FOR ALL CATEGORY
class AllCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    sub_category = models.ForeignKey("SubCategory", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title


#MODELS FOR INCLUSION
class Inclusion(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

#MODELS FOR BLOGS
class Blogs(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    content = RichTextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    cover_image = models.FileField(upload_to="blogs_images", null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
