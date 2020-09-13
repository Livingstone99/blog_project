from .import views
from django.urls import path
urlpatterns = [
    path('',views.allblogs, name = 'allblogs'),
    path('<str:pk>', views.blog_details, name='post'),
    path('<str:pk>/comment', views.add_comment_to_post, name='comment')
]