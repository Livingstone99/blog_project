from django.shortcuts import render, redirect
from django.contrib import messages
from.models import Job
from .form import FeedBackForm
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
def home(request):
    form = FeedBackForm
    jobs = Job.objects.all

    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            visitor = form.cleaned_data.get('name')
            messages.success(request, "ok "+ visitor.title() +", thanks for reaching out!")
            # return redirect('home')

    return render(request, 'projects/better.html',{"jobs":jobs, 'form':form})
