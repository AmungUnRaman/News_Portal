from django.urls import path
from . views import Posts, PostDetail, PostCreate


urlpatterns = [
    path('', Posts.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    #path('create', PostCreate.as_view(), name='newpost'),
    ]