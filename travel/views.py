from django.shortcuts import render


#===================================== views for bikingfirst front end =================================

def FrontIndexPageView(request):
    context = {}
    return render(request,'site/index.html', context)
