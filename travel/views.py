from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from travel.forms import (
    AddCategoryForm,
)
from travel.models import (
    Category,
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





