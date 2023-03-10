from django.urls import path
from .views import (
    RecipeListView,
    RecipeUpdateView, # new
    RecipeDetailView, # new
    RecipeDeleteView, # new
    RecipeCreateView,
    RecipeCommentView,
)

urlpatterns = [
    path('<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('<int:pk>/edit', RecipeUpdateView.as_view(), name="recipe_edit"),
    path('<int:pk>/delete', RecipeDeleteView.as_view(), name="recipe_delete"),
    path('new/', RecipeCreateView.as_view(), name="recipe_new"),
    path('<int:pk>/comment/new', RecipeCommentView.as_view(), name="recipe_new_comment"),
    path('', RecipeListView.as_view(), name='recipe_list'),
]
