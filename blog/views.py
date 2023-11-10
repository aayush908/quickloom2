from django.shortcuts import render , HttpResponse , redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def bloghome(request):
    allpost = Post.objects.all()
    context = {'allpost' : allpost}
    return render(request ,'blog/blog.html' , context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")

