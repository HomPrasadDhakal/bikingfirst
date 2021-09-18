from django.db import models

# MODELS FOR CATEGORY SUB CATEGORY & ALL CATEGORY

#MODELS FOR CATEGORY
class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.tite
    
#MODELS FOR SUB CATEGORY
class SubCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.tite


#MODELS FOR ALL CATEGORY
class AllCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    sub_category = models.ForeignKey("SubCategory", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.tite

    