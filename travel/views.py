from django.forms.fields import ChoiceField
from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from travel.forms import (
    AddCategoryForm,
    AddSubCategoryForm,
    AddAllCategoryForm,
    AddInclusionForm,
    AddBlogsForm,
    SliderImgForm,
    AboutUsForm,
    AddPackagesForm,
    AddPackagesImagesFrom,
    ContactUsForm,
)
from travel.models import (
    Blogs,
    Category,
    SubCategory,
    AllCategory,
    Inclusion,
    SliderImage,
    AboutusDetail,
    ContactDetail,
    Packages,
    PackagesGallary,
)
from accounts.models import user
import datetime


#===================================== views for bikingfirst front end =================================

def FrontIndexPageView(request):
    contactlist = ContactDetail.objects.all()
    sliderimage = SliderImage.objects.all()
    aboutus = AboutusDetail.objects.all()
    packages = Packages.objects.all().order_by('-id')[:9]
    upcomming_pack = Packages.objects.filter(starting_date__gte=datetime.date.today())
    latest_blogs = Blogs.objects.all().order_by('-id')[:4]
    context = {"contactlist":contactlist,
            'sliderimage':sliderimage,
            "aboutus":aboutus,
            "packages":packages,
            "upcomming_pack":upcomming_pack,
            "latest_blogs":latest_blogs,
        }
    return render(request,'site/index.html', context)


def ContactUsPage(request):
    contactlist = ContactDetail.objects.all()
    context = {"contactlist":contactlist}
    return render(request,"site/contact/contact.html", context)

def AboutusPage(request):
    aboutus = AboutusDetail.objects.all()
    contactlist = ContactDetail.objects.all()
    context = {"aboutus":aboutus,"contactlist":contactlist}
    return render(request,"site/contact/aboutus.html", context)


def BlogsPage(request):
    contactlist = ContactDetail.objects.all()
    bloglist = Blogs.objects.all().order_by('-id')
    context = {"bloglist":bloglist, "contactlist":contactlist}
    return render(request,"site/blog/bloglist.html", context)


def BlogDetailPage(request, pk):
    detailblog = Blogs.objects.get(id=pk)
    contactlist = ContactDetail.objects.all()
    context = {"contactlist":contactlist, "detailblog":detailblog}
    return render(request,"site/blog/blogdetail.html", context)


#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################





#=================================== views for bikingfirst admin pannel==================================
#login views
def BackEndLogin(request):
    return render(request,'admin/login.html')

def LoginProcess(request):
    email=request.POST.get("email")
    password=request.POST.get("password")

    user=authenticate(request=request,email=email,password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("backenddashbaord"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("loginpage"))

#logout view
def logoutprocess(request):
    logout(request)
    messages.success(request,"your successfully logout !")
    return HttpResponseRedirect(reverse("loginpage"))

#backend dashboard view
@login_required(login_url='loginpage')
def BackEndPageView(request):
    context = {}
    return render(request,"admin/index.html", context)

#=========================== views for category============================================

@login_required(login_url="loginpage")
def AddCategory(request):
    if request.user.is_superuser:
        form = AddCategoryForm()
        if request.method=='POST':
            form = AddCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Successfully Created category!!!")
                return redirect('addcategory')
    context = {'form':form}
    return render(request,"admin/category/addcategory.html", context)


@login_required(login_url='loginpage')
def CategorylistView(request):
    if request.user.is_superuser:
        categorylist = Category.objects.all().order_by('-created_at')
    context = {"categorylist":categorylist}
    return render(request, "admin/category/categorylist.html", context)


@login_required(login_url="loginpage")
def DeleteCategoryView(request, pk):
    if request.user.is_superuser:
        category = Category.objects.get(id=pk)
        category.delete()
    return redirect('categorylist')



@login_required(login_url='loginpage')
def UpdatecategoryView(request, pk):
    if request.user.is_superuser:
        category = Category.objects.get(id=pk)
        form = AddCategoryForm(instance=category)
        if request.method =="POST":
            form = AddCategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                messages.success(request,"Updated category successfully !!!")
                return redirect('categorylist')
    context = {'form':form}
    return render(request, "admin/category/updatecategory.html", context)


#=========================== views for sub category============================================

@login_required(login_url="loginpage")
def AddSubCategoryView(request):
    if request.user.is_superuser:
        form = AddSubCategoryForm()
        if request.method =="POST":
            form = AddSubCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully added subcategory")
                return redirect('subcategorylist')
            else:
                messages.error(request,"cannot add subcategory please try again!!!")
        context ={'form':form}
    return render(request, "admin/subcategory/addsubcategory.html", context)


@login_required(login_url='loginpage')
def SubCategoryListView(request):
    if request.user.is_superuser:
        subcatlist = SubCategory.objects.all()
        context= {'subcatlist':subcatlist}
    return render(request,"admin/subcategory/subcategorylist.html", context)




@login_required(login_url='loginpage')
def DeleteSubCateogryView(request, pk):
    if request.user.is_superuser:
        deletesubcat = SubCategory.objects.get(id=pk)
        deletesubcat.delete()
    return redirect('subcategorylist')


@login_required(login_url="loginpage")
def UpdateSubCategoryView(request, pk):
    if request.user.is_superuser:
        subcat = SubCategory.objects.get(id=pk)
        form = AddSubCategoryForm(instance=subcat)
        if request.method == "POST":
            form = AddSubCategoryForm(request.POST, instance=subcat)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully updated subcategory !!!")
                return redirect('subcategorylist')
        context = {'form':form}
    return render(request,"admin/subcategory/updatesubcategory.html", context)



#=========================== views for all category============================================
@login_required(login_url="loginpage")
def AddAllCategoryView(request):
    if request.user.is_superuser:
        form = AddAllCategoryForm()
        if request.method =="POST":
            form = AddAllCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully added all category")
                return redirect('allcategorylist')
            else:
                messages.error(request,"cannot add allcategory please try again!!!")
        context ={'form':form}
    return render(request, "admin/allcategory/addallcategory.html", context)


@login_required(login_url='loginpage')
def allCategoryListView(request):
    if request.user.is_superuser:
        allcatlist = AllCategory.objects.all()
        context= {'allcatlist':allcatlist}
    return render(request,"admin/allcategory/allcategorylist.html", context)



@login_required(login_url='loginpage')
def DeleteSAllCateogryView(request, pk):
    if request.user.is_superuser:
        deleteallcat = AllCategory.objects.get(id=pk)
        deleteallcat.delete()
    return redirect('allcategorylist')



@login_required(login_url="loginpage")
def UpdateallCategoryView(request, pk):
    if request.user.is_superuser:
        allcat = AllCategory.objects.get(id=pk)
        form = AddAllCategoryForm(instance=allcat)
        if request.method == "POST":
            form = AddAllCategoryForm(request.POST, instance=allcat)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully updated allcategory !!!")
                return redirect('allcategorylist')
        context = {'form':form}
    return render(request,"admin/allcategory/updateallcategory.html", context)


#=========================== views for Inclusion============================================


@login_required(login_url="loginpage")
def AddAllInslucionView(request):
    if request.user.is_superuser:
        form = AddInclusionForm()
        if request.method =="POST":
            form = AddInclusionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully added inclusion")
                return redirect('inclusionlist')
            else:
                messages.error(request,"cannot add inclusion please try again!!!")
        context ={'form':form}
    return render(request, "admin/inclusion/addinclusion.html", context)


@login_required(login_url='loginpage')
def InslucionListView(request):
    if request.user.is_superuser:
        allinclusion = Inclusion.objects.all()
        context= {'allinclusion':allinclusion}
    return render(request,"admin/inclusion/inclusionlist.html", context)



@login_required(login_url='loginpage')
def DeleteSInclusionView(request, pk):
    if request.user.is_superuser:
        deleteinclusion = Inclusion.objects.get(id=pk)
        deleteinclusion.delete()
    return redirect('inclusionlist')



@login_required(login_url="loginpage")
def UpdateInclusionView(request, pk):
    if request.user.is_superuser:
        allinc = Inclusion.objects.get(id=pk)
        form = AddInclusionForm(instance=allinc)
        if request.method == "POST":
            form = AddInclusionForm(request.POST, instance=allinc)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully updated inclusion !!!")
                return redirect('inclusionlist')
        context = {'form':form}
    return render(request,"admin/inclusion/updateinclusion.html", context)


#=========================== views for blogs============================================


@login_required(login_url="loginpage")
def AddBlogsView(request):
    if request.user.is_superuser:
        form = AddBlogsForm()
        if request.method =="POST":
            form = AddBlogsForm(request.POST, request.FILES)
            if form.is_valid():
                blogs = form.save(commit=False)
                blogs.author = request.user
                blogs.save()
                messages.success(request,"successfully added blogs")
                return redirect('blogslist')
            else:
                messages.error(request,"cannot add blog please try again!!!")
        context ={'form':form}
    return render(request, "admin/blogs/addblogs.html", context)
    


@login_required(login_url='loginpage')
def BlogsListView(request):
    if request.user.is_superuser:
        allblogs = Blogs.objects.all().order_by("-created_at")
        context= {'allblogs':allblogs}
    return render(request,"admin/blogs/bloglist.html", context)



@login_required(login_url='loginpage')
def DeleteSBlogsView(request, pk):
    if request.user.is_superuser:
        deleteblogs = Blogs.objects.get(id=pk)
        deleteblogs.delete()
    return redirect('blogslist')



@login_required(login_url="loginpage")
def UpdateBlogsView(request, pk):
    if request.user.is_superuser:
        blog = Blogs.objects.get(id=pk)
        form = AddBlogsForm(instance=blog)
        if request.method == "POST":
            form = AddBlogsForm(request.POST, instance=blog)
            if form.is_valid():
                blogs = form.save(commit=False)
                blogs.author == request.user
                blogs.save()
                messages.success(request,"successfully updated blogs !!!")
                return redirect('blogslist')
        context = {'form':form}
    return render(request,"admin/blogs/updateblogs.html", context)




#=========================== views for slider images ============================================


@login_required(login_url="loginpage")
def AddSliderImgView(request):
    if request.user.is_superuser:
        form = SliderImgForm()
        if request.method =="POST":
            form = SliderImgForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully added slider image")
                return redirect('imagesliderlist')
            else:
                messages.error(request,"cannot add slider image please try again!!!")
        context ={'form':form}
    return render(request, "admin/sliderimage/addsliderimg.html", context)


@login_required(login_url='loginpage')
def SliderImgListView(request):
    if request.user.is_superuser:
        allsliderimg = SliderImage.objects.all().order_by("-created_at")
        context= {'allsliderimg':allsliderimg}
    return render(request,"admin/sliderimage/sliderimagelist.html", context)



@login_required(login_url='loginpage')
def DeleteSLiderImgView(request, pk):
    if request.user.is_superuser:
        deletesliderimage = SliderImage.objects.get(id=pk)
        deletesliderimage.delete()
    return redirect('imagesliderlist')



@login_required(login_url="loginpage")
def UpdateSliderImgView(request, pk):
    if request.user.is_superuser:
        sliderimg = SliderImage.objects.get(id=pk)
        form = SliderImgForm(instance=sliderimg)
        if request.method == "POST":
            form = SliderImgForm(request.POST, request.FILES, instance=sliderimg)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully updated slider image !!!")
                return redirect('imagesliderlist')
        context = {'form':form}
    return render(request,"admin/sliderimage/updatesliderimg.html", context)



#=========================== views for about us  ============================================


@login_required(login_url="loginpage")
def AddAboutusVIew(request):
    if request.user.is_superuser:
        form = AboutUsForm()
        if request.method =="POST":
            form = AboutUsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully added aboutus")
                return redirect('aboutuslist')
            else:
                messages.error(request,"cannot add aboutus please try again!!!")
        context ={'form':form}
    return render(request, "admin/aboutus/addaboutus.html", context)


@login_required(login_url='loginpage')
def AboutusList(request):
    if request.user.is_superuser:
        allaboutus = AboutusDetail.objects.all().order_by("-created_at")
        context= {'allaboutus':allaboutus}
    return render(request,"admin/aboutus/aboutuslist.html", context)



@login_required(login_url='loginpage')
def DeleteAboutusView(request, pk):
    if request.user.is_superuser:
        deleteaboutus = AboutusDetail.objects.get(id=pk)
        deleteaboutus.delete()
    return redirect('aboutuslist')


@login_required(login_url="loginpage")
def UpdateAboutusView(request, pk):
    if request.user.is_superuser:
        ab = AboutusDetail.objects.get(id=pk)
        form = AboutUsForm(instance=ab)
        if request.method == "POST":
            form = AboutUsForm(request.POST, request.FILES, instance=ab)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully updated aboutus !!!")
                return redirect('aboutuslist')
    context = {'form':form}
    return render(request,"admin/aboutus/updateaboutus.html", context)



#=========================== views for contact details  ============================================


@login_required(login_url="loginpage")
def AddContactView(request):
    if request.user.is_superuser:
        form = ContactUsForm()
        if request.method =="POST":
            form = ContactUsForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully added contact details")
                return redirect('contactdetailslist')
            else:
                messages.error(request,"cannot add contactdetails  please try again!!!")
        context ={'form':form}
    return render(request, "admin/contact/addcontact.html", context)


@login_required(login_url='loginpage')
def ContactusList(request):
    if request.user.is_superuser:
        allcontact = ContactDetail.objects.all().order_by("-created_at")
        context= {'allcontact':allcontact}
    return render(request,"admin/contact/contactlist.html", context)



@login_required(login_url='loginpage')
def DeleteContactus(request, pk):
    if request.user.is_superuser:
        deletecontacts = ContactDetail.objects.get(id=pk)
        deletecontacts.delete()
    return redirect('contactdetailslist')


@login_required(login_url="loginpage")
def UpdateContactusview(request, pk):
    if request.user.is_superuser:
        contact = ContactDetail.objects.get(id=pk)
        form = ContactUsForm(instance=contact)
        if request.method == "POST":
            form = ContactUsForm(request.POST, instance=contact)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully updated contact details !!!")
                return redirect('contactdetailslist')
    context = {'form':form}
    return render(request,"admin/contact/updatecontact.html", context)



#=========================== views for packages  ============================================


@login_required(login_url="loginpage")
def AddPackagesView(request):
    if request.user.is_superuser:
        form = AddPackagesForm()
        if request.method =="POST":
            form = AddPackagesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully added Packages")
                return redirect('packageslist')
            else:
                messages.error(request,"cannot add packages  please try again!!!")
        context ={'form':form}
    return render(request, "admin/packages/addppackages.html", context)


@login_required(login_url='loginpage')
def PackagesList(request):
    if request.user.is_superuser:
        allpack = Packages.objects.all().order_by("-created_at")
        context= {'allpack':allpack}
    return render(request,"admin/packages/packlist.html", context)



@login_required(login_url='loginpage')
def Deletepackages(request, pk):
    if request.user.is_superuser:
        deletepack = Packages.objects.get(id=pk)
        deletepack.delete()
    return redirect('packageslist')


@login_required(login_url="loginpage")
def UpdatePakagesview(request, pk):
    if request.user.is_superuser:
        pack = Packages.objects.get(id=pk)
        form = AddPackagesForm(instance=pack)
        if request.method == "POST":
            form = AddPackagesForm(request.POST, request.FILES, instance=pack)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully updated packages !!!")
                return redirect('packageslist')
    context = {'form':form}
    return render(request,"admin/packages/updatepackages.html", context)

#=========================== views for packages images gallary  ============================================


@login_required(login_url="loginpage")
def AddPackagesImageView(request):
    if request.user.is_superuser:
        form = AddPackagesImagesFrom()
        if request.method =="POST":
            form = AddPackagesImagesFrom(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,"successfully added Packages images")
                return redirect('packagesimageslist')
            else:
                messages.error(request,"cannot add packages images  please try again!!!")
        context ={'form':form}
    return render(request, "admin/packages/addppackagesimages.html", context)


@login_required(login_url='loginpage')
def PackagesImageList(request):
    if request.user.is_superuser:
        Allpackimages = PackagesGallary.objects.all()
        context= {'Allpackimages':Allpackimages}
    return render(request,"admin/packages/packimageslist.html", context)



@login_required(login_url='loginpage')
def DeletepackagesImages(request, pk):
    if request.user.is_superuser:
        deletepackimage = PackagesGallary.objects.get(id=pk)
        deletepackimage.delete()
    return redirect('packagesimageslist')

#===================================== views for listing admin user=================================


@login_required(login_url='loginpage')
def ListingAdminUser(request):
    if request.user.is_superuser:
        admin = user.objects.filter(is_superuser=True)
        context = {'admin':admin}
    return render(request,"admin/user/adminlist.html", context)


@login_required(login_url="loginpage")
def ListingNormalUser(request):
    if request.user.is_superuser:
        normaluser = user.objects.filter(is_superuser=False)
        context = {"normaluser":normaluser}
    return render(request,"admin/user/normaluser.html", context)