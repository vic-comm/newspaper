from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
    template_name = 'article_list.html'
    model = Article

class ArticleEditView(UpdateView):
    template_name = 'article_edit.html'
    model = Article
    fields = ('title', 'body')

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    model= Article
    success_url = reverse_lazy('article_list')

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    model = Article

class ArticleCreateView(CreateView):
    template_name = 'article_new.html'
    model = Article
    fields = ('title', 'author', 'body')
