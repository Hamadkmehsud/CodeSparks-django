# from django.http import HttpResponseRedirect
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index.as_view(), name='main'),
    path('all-posts/', views.AllPosts.as_view(), name="all-posts"),
    path('all-posts/<slug:slug>/', views.PostDetails.as_view(), name='post-details'),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path('about-us/' ,views.about_us , name="about-us"),

    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
