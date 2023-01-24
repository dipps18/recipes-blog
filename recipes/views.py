from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from .models import Recipe, Comment


class RecipeHomeView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'home.html'


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('recipe_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe_create.html'
    fields = ('title', 'description', 'steps', 'image', 'ingredients')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ('title', 'description', 'steps', 'image', 'ingredients')
    template_name = 'recipe_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class RecipeCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('comment',)
    template_name = 'recipe_new_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super(RecipeCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.kwargs['pk']})


