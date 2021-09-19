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
)
from travel.models import (
    Blogs,
    Category,
    SubCategory,
    AllCategory,
    Inclusion,
    SliderImage,
)



#===================================== views for bikingfirst front end =================================

def FrontIndexPageView(request):
    context = {}
    return render(request,'site/index.html', context)



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