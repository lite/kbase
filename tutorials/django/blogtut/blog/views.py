from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from dynamicresponse.response import *

from forms import *
from models import *

from django.views.decorators.csrf import csrf_exempt

@ csrf_exempt
def index(request):
    """Lists all blog post."""
    
    if request.method == 'POST':
        post = BlogPost.objects.create(title=request.POST.get("title"), text=request.POST.get("text"))
        post.save()
        form = BlogPostForm(request.POST, instance=post)
    else:
        form = BlogPostForm(instance=None)
    
    posts = BlogPost.objects.all()
    return SerializeOrRender('blog/index.html', { 'posts': posts }, extra={ 'form': form })

def list_posts(request):
    """Lists all blog post."""
    
    posts = BlogPost.objects.all()
    return SerializeOrRender('blog/list_posts.html', { 'posts': posts })

def post(request, post_id=None):
    """Displays, creates or updates a blog post."""
    
    post = None
    if post_id:
        post = get_object_or_404(BlogPost.objects.all(), pk=post_id)

    if request.method == 'POST':
        
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return SerializeOrRedirect(reverse('list_posts'), { 'post': post })
            
    else:
        
        form = BlogPostForm(instance=post)
    
    return SerializeOrRender('blog/post.html', { 'post': post }, extra={ 'form': form })
    
def delete_post(request, post_id):
    """Deletes the blog post."""
    
    post = get_object_or_404(BlogPost.objects.all(), pk=post_id)
    
    if request.method == 'POST':

        post.delete()
        return SerializeOrRedirect(reverse('list_posts'), {}, status=CR_DELETED)
    
    else:
        
        return SerializeOrRender('blog/delete_post.html', { 'post': post }, status=CR_CONFIRM)
