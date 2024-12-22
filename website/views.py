
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,Contact_Form
from django.contrib import messages


def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request,'website/about.html')



