from django.shortcuts import  render, redirect
from accounts.forms import FormPasswordChange
from travel.models import *


def AdminPasswordChangeView(request):
    packages_count = Packages.objects.all().count()
    booked_packages_count = BookPackages.objects.all().count()
    total_user_count = user.objects.filter(is_superuser=False).count()
    blog_count = Blogs.objects.all().count()
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = FormPasswordChange(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('backenddashbaord')
        else:
            fm = FormPasswordChange(user=request.user)
        return render(request,"admin/changepassword/changepassword.html",{"form":fm,"packages_count":packages_count,"booked_packages_count":booked_packages_count,"total_user_count":total_user_count,"blog_count":blog_count})
    else:
        return redirect('loginpage')