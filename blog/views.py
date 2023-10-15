from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpRequest


def index(request):
    return render(request, "blog/index.html")

def blog_visit(request):
    return render(request, 'blog/blog_page.html')

def about_page_redirect(request):
    return render(request, 'blog/about_page.html')

def feedback(request):
    return render(request, 'blog/feedback.html')