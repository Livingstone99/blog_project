from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog,Comment, Category
from .form import CommentForm
from django.core.paginator import Paginator
# Create your views here.

def allblogs(request):

    article = Blog.objects.order_by('-id')
    paginator = Paginator(article, 5)
    category = Category.objects.all()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/nav.html', {"page_obj":page_obj, 'caty':category})

def blog_tag(request, pk):
    blog = Blog.objects.filter(post_category = pk)

    paginator = Paginator(blog, 5)
    category = Category.objects.all()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/nav.html', {"page_obj":page_obj, 'caty':category})

def blog_details(request, pk):
    # comment = Comment.comment.filter(parent_is_null = True)
    blog_post = Blog.objects.get(id = pk)
    category = Category.objects.all()
    comments = Comment.objects.all().filter(post_id= pk)
    form = CommentForm()
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        name = request.POST['name']
        comment = request.POST['comment']
        comments.create(name=name, body=comment, post = post)
        # if form.is_valid():
        #     comment = form.save(commit=False)
        #     comment.post = post
        #     comment.save()
        #     return redirect('post', pk=post.pk)
        #
        #     form.save()

    # return render(request, 'blog/posts.html',{'post':blog_post, 'form': form,'comments':comments})
    return render(request, 'blog/single.html', {'post':blog_post, 'category':category, 'comments':comments})
def add_comment_to_post(request, pk):
    pass