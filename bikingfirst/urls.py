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
from accounts import views as acc

#--------------------- imports for passsword rest ------------------------------------
from django.contrib.auth import views as auth_views
#--------------------- imports for passsword rest ------------------------------------
urlpatterns = [

#=========================Route for front End=======================================
#=========================Route for front End=======================================
#=========================Route for front End=======================================
    path('', a.FrontIndexPageView, name="frontendhome"),
    path('contact_us/', a.ContactUsPage, name="contactus"),
    path('about_us/', a.AboutusPage, name="aboutus"),
    #--------------------route for blog-------------------------------------------
    path('bloglist/', a.BlogsPage, name="bloglist"),
    path('detail_blog/<str:pk>', a.BlogDetailPage, name="blogdetails"),
    #---------------------Route for Packages category----------------------------
    path('packages_category/<str:pk>', a.PackageCategory, name="packagescategory"),
    path('packages_details/<str:pk>', a.PackageDetails, name="packagesdetails"),
    path('all_packages/', a.Allpackages, name="allpackages"),
    #-----------------------Route for booking packages--------------------------
    path('booking_packages/<str:pk>', a.BookingPack, name="bookingpackages"),
    #-----------------------Route for user login --------------------------------
    path('userlogin/', a.UserLogin, name="userlogin"),
    path('userloginprocess/', a.UserloginProcess, name="userloginprocess"),
    path('userlogoutprocess/', a.UserlogoutProcess, name="userlogoutprocess"),
    #-----------------------Route for user registration packages------------------------------
    path('usersignup/', a.UserRegistration, name="signupuser"),
    #-----------------------Route for search packages------------------------------
    path('packagessearch/',a.Searchpack, name="searchpackages"),

    #-------------------------ROute for user Profile------------------------------
    path('userprofile/', a.UserProfile, name="userprofile"),
    path('update_profile/', a.UserProfileUpdate, name="updateuserprofile"),
    path('my_pack/', a.MyPackView, name="mypack"),


#=========================Route for Back End =======================================
#=========================Route for Back End =======================================
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
    path('add_sub_category/',a.AddSubCategoryView, name="addsubcategory"),
    path('sub_category_list/',a.SubCategoryListView, name="subcategorylist"),
    path('delete_sub_category/<str:pk>',a.DeleteSubCateogryView, name="deletesubcateogry"),
    path('update_sub_category/<str:pk>',a.UpdateSubCategoryView, name="updatesubcateogry"),

#-----------------------Route for all category--------------------------------------------- 
    path('add_all_category/',a.AddAllCategoryView, name="addallcategory"),
    path('all_category_list/',a.allCategoryListView, name="allcategorylist"),
    path('delete_all_category/<str:pk>',a.DeleteSAllCateogryView, name="deleteallcategory"),
    path('update_all_category/<str:pk>',a.UpdateallCategoryView, name="updateallcategory"),

#-----------------------Route for Inclusion--------------------------------------------- 
    path('add_inclusion/',a.AddAllInslucionView, name="addinclusion"),
    path('inclusion_list/',a.InslucionListView, name="inclusionlist"),
    path('delete_inclusion/<str:pk>',a.DeleteSInclusionView, name="deleteinclusion"),
    path('update_inclusion/<str:pk>',a.UpdateInclusionView, name="updateinclusion"),

#-----------------------Route for Blogs--------------------------------------------- 

    path('add_blog/',a.AddBlogsView, name="addblogs"),
    path('blogs_list/',a.BlogsListView, name="blogslist"),
    path('delete_blogs/<str:pk>',a.DeleteSBlogsView, name="deleteblogs"),
    path('update_blogs/<str:pk>',a.UpdateBlogsView, name="updateblogs"),

#-----------------------Route for imageslider--------------------------------------------- 

    path('add_imageslider/',a.AddSliderImgView, name="addimageslider"),
    path('imageslider_list/',a.SliderImgListView, name="imagesliderlist"),
    path('delete_imageslider/<str:pk>',a.DeleteSLiderImgView, name="deleteimageslider"),
    path('update_imageslider/<str:pk>',a.UpdateSliderImgView, name="updateimageslider"),


#-----------------------Route for aboutus--------------------------------------------- 
    path('add_aboutus/',a.AddAboutusVIew, name="addaboutus"),
    path('aboutus_list/',a.AboutusList, name="aboutuslist"),
    path('delete_aboutus/<str:pk>',a.DeleteAboutusView, name="deleteaboutus"),
    path('update_aboutus/<str:pk>',a.UpdateAboutusView, name="updateaboutus"),


#-----------------------Route for contact detials--------------------------------------------- 
    path('add_contactdetails/',a.AddContactView, name="addcontactdetails"),
    path('contact_list/',a.ContactusList, name="contactdetailslist"),
    path('delete_contact/<str:pk>',a.DeleteContactus, name="deletecontactdetails"),
    path('update_contact/<str:pk>',a.UpdateContactusview, name="updatecontactdetails"),

#-----------------------Route for Packages--------------------------------------------- 
    path('add_packages/',a.AddPackagesView, name="addpackages"),
    path('packages_list/',a.PackagesList, name="packageslist"),
    path('delete_packages/<str:pk>',a.Deletepackages, name="deletepackages"),
    path('update_packages/<str:pk>',a.UpdatePakagesview, name="updatepackages"),
    
#-----------------------Route for booked packages-----------------------------------
    path('list_of_booked_packages', a.BookingPackagesList, name="bookedpackages"),
    path('details_of_booked_packages/<str:pk>', a.BookingDetails, name="detailsbookedpackages"),
#-----------------------Route for admin/user listing-----------------------------------

    path('admin_user/', a.ListingAdminUser, name="adminlisting"),
    path('normal_user/', a.ListingNormalUser, name="normaluser"),

#---------------------Route for inquirylist---------------------------------------------
    path('inquirylist/', a.InquiryList, name="inquirylist"),
    path('inquirylist/<str:pk>', a.InquirylistDetail, name="inquirylistdetail"),

#--------------------ROute for change password----------------------------------------------
    path('changepassword/', acc.AdminPasswordChangeView, name="AdminPasswordChangeView"),


#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
#===================================================================================================================

#---------------------------- Route for password rest for user-----------------------------------------------------
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

