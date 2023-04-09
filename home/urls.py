from django.urls import path
from home import views

urlpatterns = [
    # Routes
    path("", views.home, name='home'),
    path("<int:pk>", views.articleDetail, name='article-detail'),
    path("add-article", views.addArticle, name='add-article'),
    path("<int:pk>/update-article/", views.updateArticle, name='update-article'),
    path("<int:pk>/delete-article/", views.deleteArticle, name='delete-article'),
    path("logout/", views.logoutUser, name='logout')
]