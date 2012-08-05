from blog.models import Post
from django.shortcuts import render_to_response

def tag_page(request,tag):
    
    posts=Post.objects.filter(tags__name=tag)
    return render_to_response("tag_page.html",{"posts":posts,"tag":tag})
    