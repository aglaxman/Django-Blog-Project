

from django.shortcuts import render
from blogs.models import Category,Blog
from assignments.models import About

def home (req):

    featured_posts = Blog.objects.filter(is_featured = True , status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status = 'Published').order_by('updated_at')
    try:
        about = About.objects.first()
        print('about:',about)
    except:
        about = None
    context = {
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about
    }
    return render(req,'home.html',context)