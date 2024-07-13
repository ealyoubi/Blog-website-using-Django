from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('user/', views.list_users, name='list_users'),
    path('post/', views.blogs_view, name='blogs'),
    path('post/<int:postid>/', views.blog_details_view, name='blog_details'),
    path('category/', views.categories_view, name='categories'),
    path('comments/', views.comments_view, name='comments'),
#path('post/<int:postid>/', views.post_details_view, name='post_details'),
    #path('post/', views.post, name='post'),
    #path('category/', views.category, name='category'),
    #path('members/details/<int:id>', views.details, name='details'),
]

