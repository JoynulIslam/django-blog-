from django.urls import path,include
from dashboards.views import dashboard,categories,add_category,edit_category,delete_category

urlpatterns = [
    path('',dashboard , name='dashboard'),
    path('categories/',categories , name='categories'),
    path('categories/add',add_category , name='add_category'),
    path('categories/edit/<int:pk>/',edit_category , name='edit_category'),
    path('categories/delete/<int:pk>/', delete_category , name='delete_category'),
]
