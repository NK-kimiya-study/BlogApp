from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'blogapp'

urlpatterns = [
    path('',views.IndexViews.as_view(),name = 'index'),
    path('create/', views.create_post, name='create_post'),
    path('post-detail/<int:pk>',views.DetailView.as_view(), name='post_detail'),
    path('mypage/',views.MypageView.as_view(), name='mypage'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_delete'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('user/<int:user_id>/', views.user_posts_and_profile, name='user_posts_and_profile'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('share-group/', views.create_group, name='create_group'),
    path('group-list',views.GroupList.as_view(),name = 'group_list'),
    path('group-user-list/<int:user_id>/', views.user_group_and_profile, name='user_group_and_profile'),
    path('mypage-group/',views.MypageGroupView.as_view(), name='mypage-group'),
    path('group/<int:pk>/delete/',views.GroupDeleteView.as_view(),name='group_delete'),
    
    #ユーザー認証用
    path('signup/',views.SignUpView.as_view(), name='signup'),
    path('signup_success/',views.SignUpSuccessView.as_view(), name='signup_success'),
    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    
    path('logout/',
        auth_views.LogoutView.as_view(template_name='logout.html'),name='logout')
]