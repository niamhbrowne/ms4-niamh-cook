from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('packages/', views.packages, name='packages'),
    path('baking/', views.one_package, name='one_package'),
    path('beginner/', views.two_package, name='two_package'),
    path('experienced/', views.three_package, name='three_package'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]