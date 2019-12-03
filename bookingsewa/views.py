from django.shortcuts import render
# from django.http.response import HttpResponse
# Create your views here. method views is old style letest style is class base view
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Notice
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "index.html", {"homename": "firstpage"})


def about(request):
    return render(request, "about.html", {"aboutname": "aboutpage"})


def contact(request):
    return render(request, "contact.html", {"contactname": "contactpage"})


class NoticeListView(ListView):
    model = Notice


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):

    model = Notice