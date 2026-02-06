from django.urls import path,include
from dashboards.views import dashboard,categories,add_category,edit_category,delete_category,posts,add_post,edit_post,delete_post

urlpatterns = [
    path('',dashboard , name='dashboard'),
    # Category CRUD
    path('categories/',categories , name='categories'),
    path('categories/add',add_category , name='add_category'),
    path('categories/edit/<int:pk>/',edit_category , name='edit_category'),
    path('categories/delete/<int:pk>/', delete_category , name='delete_category'),
    #Blog POST
    path('posts/',posts , name='posts'),
    path('posts/add/',add_post , name='add_post'),
    path('posts/edit/<int:pk>/',edit_post , name='edit_post'),
    path('posts/delete/<int:pk>/',delete_post , name='delete_post'),
]
