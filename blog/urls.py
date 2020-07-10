from django.urls import path
from .views import (
    home_page,
    post_detail,
    post_create,
    PostUpdate,
    PostDeleteView,
    login_page,
    logout_page,
    user_post_list,
    UsersPostListView,
    comment_page,
    about_page,
)

app_name = 'blog'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('userpost/', user_post_list, name='user_post_list'),
    path('userpost/<str:username>',
         UsersPostListView.as_view(), name='users_post_list'),
    path('new-post/', post_create, name='post_create'),
    path('comment/<int:pk>-<str:slug>/', comment_page, name='comment_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('post/<int:pk>-<str:slug>/', post_detail, name='post_detail'),
    path('post/<int:pk>-<str:slug>/update/',
         PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>-<str:slug>/delete/',
         PostDeleteView.as_view(), name='post_delete'),

]
