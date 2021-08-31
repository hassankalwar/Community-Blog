from .views import PostDetailView, PostListView

from django.urls import path
from .import views


urlpatterns = [

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('addpost/', views.addpost, name='addpost'),
    path('updatepost/<int:id>/', views.update_post, name='updatepost'),
    path('deletepost/<int:id>/', views.delete_post, name='deletepost'),
    path('', PostListView.as_view(), name='home'),
    path('showpost/<int:pk>', PostDetailView.as_view(), name='showpost')



]
