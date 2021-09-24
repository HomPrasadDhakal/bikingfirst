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
    ContactUsForm,
    BookingPackages,
    Registrationform,
    GenralInqueryForm,
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
    BookPackages,
    GenralInquery,
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
    form = GenralInqueryForm()
    if request.method =="POST":
        form = GenralInqueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thank you for contacting us we will get back to you soon.")
            return redirect("frontendhome")
        else:
            form = GenralInqueryForm()
    context = {"contactlist":contactlist,
            'sliderimage':sliderimage,
            "aboutus":aboutus,
            "packages":packages,
            "upcomming_pack":upcomming_pack,
            "latest_blogs":latest_blogs,
            "form":form,
        }
    return render(request,'site/index.html', context)

#------------------------------------ views for contact us page --------------------------------
def ContactUsPage(request):
    contactlist = ContactDetail.objects.all()
    context = {"contactlist":contactlist}
    return render(request,"site/contact/contact.html", context)

#------------------------------------------------- views for aboutus page-----------------------------
def AboutusPage(request):
    aboutus = AboutusDetail.objects.all()
    contactlist = ContactDetail.objects.all()
    context = {"aboutus":aboutus,"contactlist":contactlist}
    return render(request,"site/contact/aboutus.html", context)

#---------------------------------------------- views for blog pages ----------------------------------------
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

#------------------------------------------ views for packages pages ------------------------------------------
def PackageCategory(request, pk):
    packcat = Packages.objects.all()
    contactlist = ContactDetail.objects.all()
    pop_pack = Packages.objects.all().order_by('-views')[:5]
    context = {"packcat":packcat,"contactlist":contactlist, "pop_pack":pop_pack }
    return render(request,"site/category/packcat.html", context)


def PackageDetails(request, pk):
    i = Packages.objects.get(id=pk)
    i.views = i.views + 1
    i.save()
    simliar_package = Packages.objects.filter(all_category=i.all_category).exclude(id=pk)[:10]
    contactlist = ContactDetail.objects.all()
    context = {"contactlist":contactlist, "i":i,"simliar_package":simliar_package}
    return render(request,"site/category/packdetail.html", context)

def Allpackages(request):
    allpackages = Packages.objects.all()
    contactlist = ContactDetail.objects.all()
    pop_pack = Packages.objects.all().order_by('-views')[:5]
    context ={"allpackages":allpackages, "contactlist":contactlist,"pop_pack":pop_pack}
    return render(request,"site/category/allpackages.html", context)

#-------------------------------------------------- views for booking packages page --------------------------------

def BookingPack(request, pk):
    if request.user.is_authenticated:
        packages = Packages.objects.get(id=pk)
        form = BookingPackages()
        if request.method == "POST":
            form = BookingPackages(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.package = packages
                booking.created_by = request.user
                booking.save()
                messages.success(request,"Congratulations you have booked your Trip successfully !!!")
                return redirect('frontendhome')
    else:
        return redirect('userlogin')
    contactlist = ContactDetail.objects.all()
    context = {"contactlist":contactlist,"form":form, "packages":packages}
    return render(request,"site/booking/booking.html", context)


#---------------------------------- views for searching packages---------------------------------------------------
def Searchpack(request):
    query1 = request.GET.get('region')
    query2 = request.GET.get('title')
    region = Packages.objects.filter(region__icontains=query1)
    title = Packages.objects.filter(title__icontains=query2)
    search = region.union(title)
    contactlist = ContactDetail.objects.all()
    context = {'search':search,"query2":query2,"contactlist":contactlist}
    return render(request,'site/searching.html', context)



#----------------------------- views for user register, login and log out ------------------------------------------


def UserLogin(request):
    return render(request,"site/user/login.html")


def UserloginProcess(request):
    email=request.POST.get("email")
    password=request.POST.get("password")

    user=authenticate(request=request,email=email,password=password)
    if user is not None:
        login(request=request,user=user)
        messages.success(request,"Congratulations login in Successfully!!!")
        return HttpResponseRedirect(reverse("frontendhome"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("frontendhome"))



def UserlogoutProcess(request):
    logout(request)
    messages.success(request,"your  successfully logout !")
    return redirect('frontendhome')


def UserRegistration(request):
    form = Registrationform()
    if request.method == "POST":
        form = Registrationform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = False
            user.is_staff = False
            user.save()
            messages.success(request,"congratulation you have successfully created your account !!!")
            return redirect("userlogin")
        else:
            context = {'form':form}
            messages.error(request,"invalid details please try again !!!")
            return render(request,"site/user/registration.html", context)
    context = {'form':form}
    return render(request,"site/user/registration.html", context)


# def Inquery(request):
#     form = GenralInqueryForm()
#     if request.method =="POST":
#         form = GenralInqueryForm(request.POST):
#         if form.is_valid():
#             form.save()
#             messages.success(request,"your inquiry has been send admin will reply you as soon as possible!!!")
#             return redirect("frontendhome")
#     context = {'form':form}
#     return render(request,"site/partials/blogs.html", context)

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
    if user is not None and user.is_superuser:
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

#=================================backend dashboard view=========================================================
@login_required(login_url='loginpage')
def BackEndPageView(request):
    packages = Packages.objects.all().order_by('-id')[:10]
    most_view_packages = Packages.objects.all().order_by('-views')[:10]
    latest_booked_packages = BookPackages.objects.all().order_by('-id')[:10]
    latest_register_user = user.objects.filter(is_superuser=False).order_by('-id')[:10]
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()

    context = {'packages':packages,
                "most_view_packages":most_view_packages,
                "latest_booked_packages":latest_booked_packages,
                "latest_register_user":latest_register_user,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
                }
    return render(request,"admin/index.html", context)

#=========================== views for category============================================

@login_required(login_url="loginpage")
def AddCategory(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
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
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    categorylist = Category.objects.all().order_by('-created_at')
    context = {"categorylist":categorylist,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request, "admin/category/categorylist.html", context)


@login_required(login_url="loginpage")
def DeleteCategoryView(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('categorylist')



@login_required(login_url='loginpage')
def UpdatecategoryView(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    category = Category.objects.get(id=pk)
    form = AddCategoryForm(instance=category)
    if request.method =="POST":
        form = AddCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated category successfully !!!")
            return redirect('categorylist')
    context = {'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
            }
    return render(request, "admin/category/updatecategory.html", context)


#=========================== views for sub category============================================

@login_required(login_url="loginpage")
def AddSubCategoryView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    form = AddSubCategoryForm()
    if request.method =="POST":
        form = AddSubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully added subcategory")
            return redirect('subcategorylist')
        else:
            messages.error(request,"cannot add subcategory please try again!!!")
    context ={'form':form,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
            }
    return render(request, "admin/subcategory/addsubcategory.html", context)


@login_required(login_url='loginpage')
def SubCategoryListView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    subcatlist = SubCategory.objects.all()
    context= {'subcatlist':subcatlist,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request,"admin/subcategory/subcategorylist.html", context)




@login_required(login_url='loginpage')
def DeleteSubCateogryView(request, pk):
    deletesubcat = SubCategory.objects.get(id=pk)
    deletesubcat.delete()
    return redirect('subcategorylist')


@login_required(login_url="loginpage")
def UpdateSubCategoryView(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    subcat = SubCategory.objects.get(id=pk)
    form = AddSubCategoryForm(instance=subcat)
    if request.method == "POST":
        form = AddSubCategoryForm(request.POST, instance=subcat)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully updated subcategory !!!")
            return redirect('subcategorylist')
    context = {'form':form,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request,"admin/subcategory/updatesubcategory.html", context)



#=========================== views for all category============================================
@login_required(login_url="loginpage")
def AddAllCategoryView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    form = AddAllCategoryForm()
    if request.method =="POST":
        form = AddAllCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully added all category")
            return redirect('allcategorylist')
        else:
            messages.error(request,"cannot add allcategory please try again!!!")
    context ={'form':form,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
            }
    return render(request, "admin/allcategory/addallcategory.html", context)


@login_required(login_url='loginpage')
def allCategoryListView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    allcatlist = AllCategory.objects.all()
    context= {'allcatlist':allcatlist,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
                }
    return render(request,"admin/allcategory/allcategorylist.html", context)



@login_required(login_url='loginpage')
def DeleteSAllCateogryView(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    deleteallcat = AllCategory.objects.get(id=pk)
    deleteallcat.delete()
    return redirect('allcategorylist')



@login_required(login_url="loginpage")
def UpdateallCategoryView(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    allcat = AllCategory.objects.get(id=pk)
    form = AddAllCategoryForm(instance=allcat)
    if request.method == "POST":
        form = AddAllCategoryForm(request.POST, instance=allcat)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully updated allcategory !!!")
            return redirect('allcategorylist')
    context = {'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
            }
    return render(request,"admin/allcategory/updateallcategory.html", context)


#=========================== views for Inclusion============================================


@login_required(login_url="loginpage")
def AddAllInslucionView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    form = AddInclusionForm()
    if request.method =="POST":
        form = AddInclusionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully added inclusion")
            return redirect('inclusionlist')
        else:
            messages.error(request,"cannot add inclusion please try again!!!")
    context ={'form':form,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
            }
    return render(request, "admin/inclusion/addinclusion.html", context)


@login_required(login_url='loginpage')
def InslucionListView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    allinclusion = Inclusion.objects.all()
    context= {'allinclusion':allinclusion,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
                }
    return render(request,"admin/inclusion/inclusionlist.html", context)



@login_required(login_url='loginpage')
def DeleteSInclusionView(request, pk):
    deleteinclusion = Inclusion.objects.get(id=pk)
    deleteinclusion.delete()
    return redirect('inclusionlist')



@login_required(login_url="loginpage")
def UpdateInclusionView(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    allinc = Inclusion.objects.get(id=pk)
    form = AddInclusionForm(instance=allinc)
    if request.method == "POST":
        form = AddInclusionForm(request.POST, instance=allinc)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully updated inclusion !!!")
            return redirect('inclusionlist')
    context = {'form':form,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
                }
    return render(request,"admin/inclusion/updateinclusion.html", context)


#=========================== views for blogs============================================


@login_required(login_url="loginpage")
def AddBlogsView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
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
    context ={'form':form,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request, "admin/blogs/addblogs.html", context)



@login_required(login_url='loginpage')
def BlogsListView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    allblogs = Blogs.objects.all().order_by("-created_at")
    context= {'allblogs':allblogs,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request,"admin/blogs/bloglist.html", context)



@login_required(login_url='loginpage')
def DeleteSBlogsView(request, pk):
    deleteblogs = Blogs.objects.get(id=pk)
    deleteblogs.delete()
    return redirect('blogslist')



@login_required(login_url="loginpage")
def UpdateBlogsView(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
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
    context = {'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request,"admin/blogs/updateblogs.html", context)




#=========================== views for slider images ============================================


@login_required(login_url="loginpage")
def AddSliderImgView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    form = SliderImgForm()
    if request.method =="POST":
        form = SliderImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully added slider image")
            return redirect('imagesliderlist')
        else:
            messages.error(request,"cannot add slider image please try again!!!")
    context ={'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
        }
    return render(request, "admin/sliderimage/addsliderimg.html", context)


@login_required(login_url='loginpage')
def SliderImgListView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    allsliderimg = SliderImage.objects.all().order_by("-created_at")
    context= {'allsliderimg':allsliderimg,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request,"admin/sliderimage/sliderimagelist.html", context)



@login_required(login_url='loginpage')
def DeleteSLiderImgView(request, pk):
    deletesliderimage = SliderImage.objects.get(id=pk)
    deletesliderimage.delete()
    return redirect('imagesliderlist')



@login_required(login_url="loginpage")
def UpdateSliderImgView(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    sliderimg = SliderImage.objects.get(id=pk)
    form = SliderImgForm(instance=sliderimg)
    if request.method == "POST":
        form = SliderImgForm(request.POST, request.FILES, instance=sliderimg)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully updated slider image !!!")
            return redirect('imagesliderlist')
    context = {'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request,"admin/sliderimage/updatesliderimg.html", context)



#=========================== views for about us  ============================================


@login_required(login_url="loginpage")
def AddAboutusVIew(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    form = AboutUsForm()
    if request.method =="POST":
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully added aboutus")
            return redirect('aboutuslist')
        else:
            messages.error(request,"cannot add aboutus please try again!!!")
    context ={'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request, "admin/aboutus/addaboutus.html", context)


@login_required(login_url='loginpage')
def AboutusList(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    allaboutus = AboutusDetail.objects.all().order_by("-created_at")
    context= {'allaboutus':allaboutus,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request,"admin/aboutus/aboutuslist.html", context)



@login_required(login_url='loginpage')
def DeleteAboutusView(request, pk):
    deleteaboutus = AboutusDetail.objects.get(id=pk)
    deleteaboutus.delete()
    return redirect('aboutuslist')


@login_required(login_url="loginpage")
def UpdateAboutusView(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    ab = AboutusDetail.objects.get(id=pk)
    form = AboutUsForm(instance=ab)
    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES, instance=ab)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully updated aboutus !!!")
            return redirect('aboutuslist')
    context = {'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request,"admin/aboutus/updateaboutus.html", context)



#=========================== views for contact details  ============================================


@login_required(login_url="loginpage")
def AddContactView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    form = ContactUsForm()
    if request.method =="POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully added contact details")
            return redirect('contactdetailslist')
        else:
            messages.error(request,"cannot add contactdetails  please try again!!!")
    context ={'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request, "admin/contact/addcontact.html", context)


@login_required(login_url='loginpage')
def ContactusList(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    allcontact = ContactDetail.objects.all().order_by("-created_at")
    context= {'allcontact':allcontact,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request,"admin/contact/contactlist.html", context)



@login_required(login_url='loginpage')
def DeleteContactus(request, pk):
    deletecontacts = ContactDetail.objects.get(id=pk)
    deletecontacts.delete()
    return redirect('contactdetailslist')


@login_required(login_url="loginpage")
def UpdateContactusview(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    contact = ContactDetail.objects.get(id=pk)
    form = ContactUsForm(instance=contact)
    if request.method == "POST":
        form = ContactUsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully updated contact details !!!")
            return redirect('contactdetailslist')
    context = {'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request,"admin/contact/updatecontact.html", context)



#=========================== views for packages  ============================================


@login_required(login_url="loginpage")
def AddPackagesView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    form = AddPackagesForm()
    if request.method =="POST":
        form = AddPackagesForm(request.POST, request.FILES)
        if form.is_valid():
            pack = form.save()
            image = request.FILES.getlist("slider_images")
            for i in image:
                PackagesGallary.objects.create(packages=pack, image=i)
            messages.success(request,"successfully added Packages")
            return redirect('packageslist')
        else:
            messages.error(request,"cannot add packages  please try again!!!")
    context ={'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request, "admin/packages/addppackages.html", context)


@login_required(login_url='loginpage')
def PackagesList(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    allpack = Packages.objects.all().order_by("-created_at")
    context= {'allpack':allpack,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request,"admin/packages/packlist.html", context)



@login_required(login_url='loginpage')
def Deletepackages(request, pk):
    if request.user.is_superuser:
        deletepack = Packages.objects.get(id=pk)
        deletepack.delete()
    return redirect('packageslist')


@login_required(login_url="loginpage")
def UpdatePakagesview(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    pack = Packages.objects.get(id=pk)
    form = AddPackagesForm(instance=pack)
    if request.method == "POST":
        form = AddPackagesForm(request.POST, request.FILES, instance=pack)
        if form.is_valid():
            pack = form.save()
            image = request.FILES.getlist("slider_images")
            for i in image:
                PackagesGallary.objects.create(packages=pack, image=i)
            messages.success(request,"successfully updated packages !!!")
            return redirect('packageslist')
    context = {'form':form,
            "packages_count":packages_count,
            "booked_packages_count":booked_packages_count,
            "total_user_count":total_user_count,
            "blog_count":blog_count,
    }
    return render(request,"admin/packages/updatepackages.html", context)

#===================================== views for packages booking =================================

@login_required(login_url="loginpage")
def BookingPackagesList(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    bookingpackage = BookPackages.objects.all().order_by('-id')
    context = {"bookingpackage":bookingpackage,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request,"admin/booking/bookingpackages.html", context)


@login_required(login_url="loginpage")
def BookingDetails(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    booking_details = BookPackages.objects.get(id=pk)
    context = {"i":booking_details,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request,"admin/booking/booking-details.html", context)


#===================================== views for listing admin user=================================


@login_required(login_url='loginpage')
def ListingAdminUser(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    admin = user.objects.filter(is_superuser=True)
    context = {'admin':admin,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request,"admin/user/adminlist.html", context)


@login_required(login_url="loginpage")
def ListingNormalUser(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    normaluser = user.objects.filter(is_superuser=False)
    context = {"normaluser":normaluser,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request,"admin/user/normaluser.html", context)


@login_required(login_url="loginpage")
def InquiryList(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    InquiryList = GenralInquery.objects.all()
    context={"InquiryList":InquiryList}
    return render(request,"admin/inquiry/inquirylist.html", context)

@login_required(login_url="loginpage")
def InquirylistDetail(request, pk):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    inquirylist = GenralInquery.objects.get(id=pk)
    context = {"i":inquirylist,
                "packages_count":packages_count,
                "booked_packages_count":booked_packages_count,
                "total_user_count":total_user_count,
                "blog_count":blog_count,
    }
    return render(request,"admin/inquiry/inquirydetail.html", context)
