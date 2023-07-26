from django.shortcuts import render, redirect
from .models import People


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = People.objects.create(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")


def indexpage(request):
    data = People.objects.all()
    context = {"data" :data}
    return render(request, "index.html", context)


def aboutpage(request):
    return render(request, "about.html")


def servicespge(request):
    return render(request, "services.html")


def projectspage(request):
    return render(request, "projects.html")


def blogspage(request):
    return render(request, "blog.html")


def signup(request):
    return render(request, "signup.html")
