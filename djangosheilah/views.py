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


# function to delete data
def deleteData(request, id):
    d = People.objects.get(id=id)
    d.delete()
    return redirect("/")

    return render(request, "index.html")


# Function to update the records

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit_data = People.objects.get(id=id)
        edit_data.name = name
        edit_data.email = email
        edit_data.age = age
        edit_data.gender = gender
        edit_data.save()

        return redirect("/")

    dta = People.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)


def indexpage(request):
    data = People.objects.all()
    context = {"data": data}
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
