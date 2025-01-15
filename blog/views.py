from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment,Category
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import Comment_Form
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.template import loader

def blog_home(request,**kwargs):
    now = timezone.now()
    postss = Post.objects.filter(status = 1 , published_date__lte=now).order_by('-published_date')[:3]
    posts = Post.objects.filter(status = 1 , published_date__lte=now)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 4)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
         posts = posts.get_page(1)

    context = {'posts': posts,
               'postss': postss}
    return render(request,'blog/home.html',context)

@login_required
def blog_single(request,pid):
    now = timezone.now()
    if request.method=='POST':
        form = Comment_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your comment submited successfully.")
        else:
            messages.add_message(request, messages.ERROR, "Your comment didn't send.")
    
    postss = Post.objects.filter(status = 1 , published_date__lte=now)
    sorted_postss = postss.order_by('-published_date')
    posts = get_object_or_404(postss, id=pid)
    
    comments = Comment.objects.filter(post=posts.id,approved=1).order_by('created_date')
    all_posts = list(postss)

    current_index = all_posts.index(posts)

    pre_post = all_posts[current_index - 1] if current_index > 0 else None
    next_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None

    posts + 1
            
    form = Comment_Form()
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'postss': postss,
        'pre_post': pre_post,
        'next_post': next_post,
        'comments': comments,
        'form': form,
        'categories': categories,
        'sorted_postss':sorted_postss,
        }
               
    return render(request,'blog/single.html',context)
    

def blog_search(request):
    now = timezone.now()
    posts = Post.objects.filter(status = 1 , published_date__lte=now)
    if request.method == 'GET':
        if search_query:= request.GET.get('search'):
            posts = posts.filter(Q(content__icontains=search_query) | Q(title__icontains=search_query))
    context = {'posts': posts}
    return render(request,'blog/home.html',context)


def blog_category(request,cat_name):
    now = timezone.now()
    posts = Post.objects.filter(status = 1, published_date__lte=now)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request,'blog/home.html',context)




def robots_txt(request):
    template = loader.get_template('robots.txt')
    context = {
        'request': request,
    }
    return HttpResponse(template.render(context), content_type='text/plain')




