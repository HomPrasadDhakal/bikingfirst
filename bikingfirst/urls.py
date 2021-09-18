"""bikingfirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from travel import views as a
urlpatterns = [

#=========================Route for front End=======================================
    path('', a.FrontIndexPageView, name="frontendhome"),
#=========================Route for Back End =======================================
    path('admin/', a.BackEndLogin, name="loginpage"),
    path('loginprocess/',a.LoginProcess, name="loginprocess"),
    path('logoutprocess/',a.logoutprocess, name="logoutprocess"),
    path('dashboard/', a.BackEndPageView, name="backenddashbaord"),
#-----------------------Route for category-------------------------------------------
    path('add_category/',a.AddCategory, name="addcategory"),
    path('category_list/',a.CategorylistView, name="categorylist"),
    path('delete_category/<str:pk>',a.DeleteCategoryView, name="deletecategory"),
    path('update_category/<str:pk>',a.UpdatecategoryView, name="updatecategory"),

#-----------------------Route for sub category-------------------------------------------





] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
