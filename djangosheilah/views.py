from django.shortcuts import render, redirect


def aboutpage(request):
    return render(request, "about.html")

def servicespge(request):
    return render(request, "services.html")

def projectspage(request):
    return render(request, "projects.html")

def blogspage(request):
    return render(request, "blog.html" )