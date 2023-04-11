from django.shortcuts import render
from blog.models import Post


def get_index(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
    }
    return render(request, "blog/index.html", context=context)


def get_about(request):
    context = {
        "title": "Страница о нас"
    }
    return render(request, "blog/about.html", context=context)


def get_contacts(request):
    context = {
        "title": "Как с нами связаться"
    }
    return render(request, "blog/contacts.html", context=context)


def get_post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        "post": post,
    }
    return render(request, "blog/post_detail.html", context)



def get_delete_post(request):
    context = {
        "title": ""
    }
    return render(request, "blog/delete_post.html", context=context)


def get_update_post(request):
    context = {
        "title": ""
    }
    return render(request, "blog/update_post.html", context=context)



