from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"templapp/index.html")

def filter_example(request):
    context_dict = {"text":"Hello World","number":100}
    return render(request,"templapp/filter.html",context_dict)
