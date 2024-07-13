from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import User, Post, Category, Comment


def list_users(request):
    users = User.objects.all()
    for user in users:
        print(f"Username: {user.username}, Email: {user.email}")
    return render(request, 'users.html', {'users': users})

def blogs_view(request):
    blogs = Post.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

def blog_details_view(request, postid):
    blog = get_object_or_404(Post, postid=postid)
    return render(request, 'blogdetails.html', {'blog': blog})

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def comments_view(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})

    #def post_details_view(request, postid):
    #post = get_object_or_404(Post, id=postid)
    #return render(request, 'post_details.html', {'post': post})
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


