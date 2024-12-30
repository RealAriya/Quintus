
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from blog.models import Post
from django.utils import timezone
from website.forms import Contact_Form
from django.contrib import messages


def index_view(request):
    now = timezone.now()
    posts = Post.objects.filter(status = 1 , published_date__lte=now)[:3]

    context = {'posts': posts,
            }
    
    return render(request,'website/index.html',context)


def about_view(request):
    return render(request,'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            contact = Contact(**form.cleaned_data)
            contact.save()
            messages.add_message(request, messages.SUCCESS, "Your ticket submited successfully.")
        else:
             messages.add_message(request, messages.ERROR, "Your ticket didn't submited.")

    form = Contact_Form()

    return render(request,'website/contact.html',{'form':form})
