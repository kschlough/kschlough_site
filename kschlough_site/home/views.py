from django.shortcuts import render

def home_view(request):
    qs = BlogPost.objects.all()
    template_name = 'home.html'
    context = {'object_list': qs}
    return render(request, template_name, context)
