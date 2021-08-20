from django.shortcuts import render
from .models import BlogPost

def home_view(request):
    # home view defines QuerySet (group of objects, qs) & pipes that into list of objects as the context
    qs = BlogPost.objects.all()
    template_name = 'home.html'
    context = {'object_list': qs}
    return render(request, template_name, context)
