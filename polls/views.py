from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from polls.forms import StudentForm


def index(request):
    return HttpResponseRedirect(reverse("home"))


def home(request):
    return render(request, "index.html")


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("add_student"))
    else:
        form = StudentForm()
    context = {"form": form}
    return render(request, "student_form.html", context)
