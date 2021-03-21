from .import views
from django.urls import path
urlpatterns = [
    path('',views.allblogs, name = 'allblogs'),
    path('test/<int:pk>', views.blog_details, name='post'),
    path('caty/<int:pk>', views.blog_tag, name='caty'),
    path('<str:pk>/comment', views.add_comment_to_post, name='comment')
]