from django.shortcuts import render ,get_object_or_404
from . models import SparksModel
from django.views.generic import ListView, DetailView ,View
from .form import CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
class Index(ListView):
    template_name = "blogs/main.html"
    model = SparksModel
    ordering = ["-date"]
    context_object_name = "recent_blogs"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
class PostDetails(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved_for_later = post_id in stored_posts
        else:
          is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = SparksModel.objects.get(slug=slug)

        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blogs/post-details.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = SparksModel.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-details", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

class AllPosts(ListView):
    template_name = "blogs/all-posts.html"
    model = SparksModel
    context_object_name = "blogs_list"
    ordering = ["-date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = SparksModel.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blogs/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")
    
def about_us(request):
    return render(request,"blogs/about-us.html")


