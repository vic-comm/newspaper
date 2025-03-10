from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleEditView, ArticleDeleteView, ArticleCreateView
# Create your views here.

urlpatterns = [path('', ArticleListView.as_view(), name='article_list'),
               path("<int:pk>/delete", ArticleDeleteView.as_view(), name='article_delete'),
               path('<int:pk>/edit',ArticleEditView.as_view(), name='article_edit'),
               path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
               path('articles/new', ArticleCreateView.as_view(), name='article_new')
               ]