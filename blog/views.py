from django.shortcuts import render,redirect,get_object_or_404


# Create your views here.
from blog.models import *
from blog import forms






# Create a lists of post 
def post_list(request):
    # create an object and retrieve all blog data order by published date in descending order
    posts=Post.objects.all().order_by('-published_date')
    # create a dictionary 
    d={'posts':posts}
    # create a html page and render it with context
    return render(request,'blog_list.html',d)


# create a post_details function so that we see all the content of blog using their id
def post_details(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    return render(request,'post_details.html',{'post':post})



# create form that user can post their blog according fields
def create_blog(request):
    # create an objects sending the input elements without data
    FO=forms.BlogForm()
    #store the object in a dictionary in key, value pairs
    d={'FO':FO}
    #check form method 
    if request.method=='POST':
        # check if method is true collect data from forms and store in a variable
        FDO=forms.BlogForm(request.POST)
        #check if data is valid or correct according fields
        if FDO.is_valid():
            post=FDO.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('post_details',post_id=post.id)
    else:
        post=forms.BlogForm()

    
    return render(request,'create_blog.html',d)

