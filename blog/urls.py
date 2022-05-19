from django.urls import path

from blog import views

urlpatterns = [
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('', views.PostList.as_view()),
    # path('<int:pk>/', views.single_post_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.category_page),
]