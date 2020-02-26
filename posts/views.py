from django.shortcuts import render, redirect
from posts.models import Posts, PostsForm

# Create your views here.
def index(request):
    form = PostsForm()
    data = Posts.objects.all()
    if request.method =='POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'title' : 'Add New Posts', 'form' : form, 'rows' : data}) 
