from django.contrib.syndication.views import Feed
from models import Post

class BlogFeed(Feed):
    title = "Mysite"
    link = "/blog/feed/"
    description = "description of my blog"

    def items(self):
        return Post.objects.all().order_by("-creared")[:2]

    def item_title(self, item):
        return item.title
    
    def item_link(self, item):
        return u'/blog/%d' %item.id
        
    def item_description(self, item):
        return item.body
    