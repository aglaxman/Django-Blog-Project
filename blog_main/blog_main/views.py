

from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from assignments.models import About
from .forms import RegistrationFrom
def home (req):

    featured_posts = Blog.objects.filter(is_featured = True , status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status = 'Published').order_by('updated_at')
    try:
        about = About.objects.first()
    except:
        about = None


    context = {
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
        
    }
    return render(req,'home.html',context)


def register(req):
    if req.method == 'POST':
        form = RegistrationFrom(req.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationFrom()
    context = {
        'form' : form
    }
    return render(req, 'register.html', context)