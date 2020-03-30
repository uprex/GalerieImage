from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render
from django.template import Context, loader
from galerie_app.models import Post
from django.http import HttpResponse

def index(request):
    post_list = Post.object.all()
    return render(request, "index.html", {'post_list': post_list})