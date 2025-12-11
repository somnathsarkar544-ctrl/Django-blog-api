from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.ArticleListCreateView.as_view(),name='articles_list'),
    path('articles/feed/',views.FeedView.as_view(),name='articles_feed'),
    path('articles/<slug:slug>/',views.ArticleRetrieveUpdateDelete.as_view(),name='article_detail'),
    path('articles/<slug:slug>/favourite/',views.ArticleFavouriteToggle.as_view(),name='article_favourite'),
    

]