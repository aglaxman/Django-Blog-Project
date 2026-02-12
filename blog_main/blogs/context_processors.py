
from .models import Category
from assignments.models import SocialLink


def get_categories(req):
    categories = Category.objects.all()
    return dict(
        categories=categories 
    )



def get_sociallinks(req):
    
    sociallinks = SocialLink.objects.all()
    return dict(
        sociallinks = sociallinks
    )