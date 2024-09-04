from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import FoodRecipe
from django.http import Http404

def index(request):
    blog_title="Food Recipes"
    # getting data from foodreceipe model
    post = FoodRecipe.objects.all()
    return render(request,'index.html',{'blog_title':blog_title, 'posts': post })

def detail(request,post_id):
    # static model
    # post=next((item for item in post if item['id'] == int(post_id)), None)
    
    # getting data from model by id
    try:
        post= FoodRecipe.objects.get(pk=post_id)
    
    except FoodRecipe.DoesNotExist:
        raise Http404("Post Does not Exists ")
    
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    return render(request,'detail.html', {'post': post})

def old_url(request):
    return redirect(reverse("restaurant:new_url_page"))

def new_url(request):
    return HttpResponse("you're in new url page")