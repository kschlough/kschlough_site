from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def home_view(request):
    # home view defines QuerySet (group of objects, qs) & pipes that into list of objects as the context
    qs = BlogPost.objects.all()
    template_name = 'home.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

# single article view - object not qs
def read_article(request, slug):
    # slug should be all lower case w/ hyphens eg first-post as a unique url for the post
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'read_article.html'
    context = {'object': obj}
    return render(request, template_name, context)
