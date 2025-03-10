from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'article_list.html'
    model = Article

class ArticleEditView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    template_name = 'article_edit.html'
    model = Article
    fields = ('title', 'body')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'article_delete.html'
    model= Article
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'article_detail.html'
    model = Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_new.html'
    model = Article
    fields = ('title', 'author', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
