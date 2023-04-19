from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, Comment
from blog.forms import CommentForms
from blog.forms import PostForm


# Read/Retrieve
class IndexView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    template_name = "blog/index.html"
    # extra_context = {"title": "Главная страница"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ''
        return context


# Read/Retrieve
class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    extra_context = {"form" : CommentForms()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForms()
        return context
    
    def post(self, request, pk):
        post = Post.objects.get(pk = pk)
        form = CommentForms(request.POST)
        if form.is_valid():
            pre_saved_comment = form.save(comment=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()
        # username = request.POST.get("username_input", None)
        # text = request.POST.get("text", None)
        # if username and text:
        #     comment = Comment.objects.create(username=username, text=text, post=post)
        #     comment.save()
        return redirect("post-detail", pk)


# CREATE
class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = '/'


# # DELETE
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]


class PostDeleteConfirimView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete_confirm.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]


# UPDATE
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]


# def get_index(request):
#     posts = Post.objects.all()
#     context = {
#         "title": "Главная страница",
#         "posts": posts,
#     }
#     return render(request, "blog/index.html", context=context)

class AboutView(generic.TemplateView):
    model = Post 
    template_name = "blog/about.html"
    
    

class ContactsView(generic.TemplateView):
    model = Post
    template_name = "blog/contacts.html" 
    
    

# def get_about(request):
#     # context = {
#     #     "title": "Страница о нас"
#     # }
#     return render(request, "blog/about.html", context=None)


# def get_contacts(request):
#     context = {
#         "title": "Как с нами связаться"
#     }
#     return render(request, "blog/contacts.html", context=context)


# Read\Retrieve
# def get_post(request, pk):
#     post = Post.objects.get(id=pk)
#     context = {
#         "post": post,
#     }
#     return render(request, "blog/post_detail.html", context)


# def post_update(request):
#     return render(request, "blog/post_update.html")
#
#
# def post_create(request):
#     return render(request, "blog/post_create.html")