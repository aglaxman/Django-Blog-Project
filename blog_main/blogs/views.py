from django.shortcuts import render,get_object_or_404 ,redirect
from django.http import Http404
from .models import Blog,Category
from django.db.models import Q
from assignments.models import About




def posts_by_category(req, category_id):

    # fetch the posts that belongs to the category with the id

    posts = Blog.objects.filter(status = 'Published' ,category = category_id)

    #! try except when u want to do some costum action
    # try:
    #     category = Category.objects.get(pk = category_id)
    # except:
    #     return redirect('home')

    #! use get_object_or_404 when u wnat to use the page not found page if the cateogry doesnot exit 
    category = get_object_or_404(Category, pk = category_id)


    # fetch the about us 
    
    
    context = {
        'posts' : posts,
        'category' : category,
    }
    return render (req,'posts_by_category.html',context)




def blogs(req, slug):
    single_blog = get_object_or_404(Blog , slug = slug , status = 'Published')
    context ={
        'single_blog' : single_blog
    }
    return render(req, 'blogs.html' , context)



def search(req):
    keyword = req.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body__icontains = keyword) , status = "Published"  )
    
    context={
        'blogs' : blogs,
        'keyword' : keyword
    }
    return render(req, 'search.html',context)