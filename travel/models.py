from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from accounts.models import user

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

    
#MODELS FOR IMAGE SLIDER
class SliderImage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    image = models.FileField( upload_to="slider_image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#MODELS FOR CONTACT DETAILS
class ContactDetail(models.Model):
    sub_title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slagon

#MODELS FOR ABOUT DETAILS
class AboutusDetail(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    about_cover = models.FileField(upload_to="about_cover_image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#MODELS FOR PACKAGES
RATING = (
    ('1','ONE'),
    ('2','TWO'),
    ('3','THREE'),
    ('4','FOUR'),
    ('5','FIVE'),
)
class Packages(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.FileField(upload_to="trip_photos")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    all_category = models.ForeignKey(AllCategory, on_delete=models.CASCADE)
    Itinerary = RichTextField()
    region = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    starting_date = models.DateField()
    ending_date = models.DateField()
    Availability = models.BooleanField(default=False)
    inclusion  = models.ManyToManyField(Inclusion, related_name="package_inclusion", blank=True)
    price = models.PositiveIntegerField()
    rating = models.CharField(max_length=25, choices=RATING)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PackagesGallary(models.Model):
    packages = models.ForeignKey(Packages, on_delete=models.CASCADE)
    image = models.FileField(upload_to="packages/images")

    def __str__(self):
        return self.packages.title

#==============================================models for booking=======================================================
    
class BookPackages(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    country = models.CharField(max_length=255)
    no_of_adults = models.CharField(max_length=255)
    no_of_children = models.CharField(max_length=255)
    created_by = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title 

    

class GenralInquery(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    packages = models.ForeignKey(Packages, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)