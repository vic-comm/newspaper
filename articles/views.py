from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView
from .models import Article
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from .forms import CommentForm

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

class CommentGet(DetailView):
    template_name = 'article_detail.html'
    model = Article 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class= CommentForm
    template_name = 'article_detail'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.object
        return reverse('article_list')

class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'article_detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_new.html'
    model = Article
    fields = ('title', 'author', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
