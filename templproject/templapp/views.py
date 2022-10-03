from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "templapp/index.html")

def other(request):
    return render(request, "templapp/other.html")

def relative(request):
    return render(request, "templapp/relative_url_templates.html")

def base(request):
    # this is actually only a base template for the inheritance, but just to see it I created a view
    return render(request, "templapp/base.html")

def inheriting(request):
    return render(request, "templapp/inheriting_template.html")

def index_inheriting(request):
    return render(request,"templapp/index_inheriting.html")

def index_filter(request):
    context_dict = {"text":"Hello World","number":100}
    return render(request,"templapp/index_filter.html",context_dict)
