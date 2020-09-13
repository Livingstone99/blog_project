from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog,Comment
from .form import CommentForm

# Create your views here.
def allblogs(request):
    titles = Blog.objects.all
    return render(request, 'blog/index.html', {"titles":titles})


def blog_details(request, pk):
    # comment = Comment.comment.filter(parent_is_null = True)

    blog_post = Blog.objects.get(id = pk)
    comments = Comment.objects.all().filter(post_id= pk)
    form = CommentForm()
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', pk=post.pk)

            # form.save()

    return render(request, 'blog/posts.html',{'post':blog_post, 'form': form,'comments':comments})
def add_comment_to_post(request, pk):
    pass