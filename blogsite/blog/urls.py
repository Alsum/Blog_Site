from django.conf.urls.defaults import patterns,include,url
from django.views.generic import ListView,DetailView
from blog.models import Post
from blog.views import tag_page
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',

     url(r'^$',ListView.as_view(queryset=Post.objects.all().order_by("-creared")[:2],
                                template_name='blog.html')),
                       
     url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,
                                     template_name='post.html')),
                       
     url(r'^archive/$',ListView.as_view(queryset=Post.objects.all().order_by("-creared"),
                                template_name='archive.html')),
                       
     url(r'^tag/(?P<tag>\w+)$',tag_page), 
     
     url(r'^about/$',direct_to_template,{'template':'about.html'}), 
       
     url(r'^comments/', include('django.contrib.comments.urls')),                        
)
