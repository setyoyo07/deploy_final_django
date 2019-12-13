from django.shortcuts import render
from .models import Designer, Post, Response

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'dribble/index.html', {'posts':posts})

def explore(request):
    posts = Post.objects.all()
    return render(request, 'dribble/explore.html', {'posts':posts})

def ourdesigner(request):
    posts = Post.objects.all()
    return render(request, 'dribble/list_designer.html', {'posts':posts})

def account(request):
    posts = Post.objects.all()
    return render(request, 'dribble/account.html', {'posts':posts})

def addpost(request):
    posts = Post.objects.all()
    return render(request, 'dribble/form_post.html', {'posts':posts})

def animation(request):
    posts = Post.objects.filter(category = 'Animation')
    return render(request, 'dribble/explore.html', {'posts':posts})

def branding(request):
    posts = Post.objects.filter(category = 'Branding')
    return render(request, 'dribble/explore.html', {'posts':posts})

def ilustration(request):
    posts = Post.objects.filter(category = 'Illustration')
    return render(request, 'dribble/explore.html', {'posts':posts})

def daftar(request):
    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']
    img = request.POST['img']

    new = Designer(email=email, password=password, username=username, img=img)
    new.save()

    return render(request, 'dribble/account.html', {})

def inputpost(request):
    title = request.POST['title']
    caption = request.POST['caption']
    category = request.POST['category']
    img = request.POST['img']
    user = 1

    new = Post(designer_id=user, img=img, nama=title, caption=caption, category=category)
    new.save()

    posts = Post.objects.all()
    return render(request, 'dribble/explore.html', {'posts':posts})