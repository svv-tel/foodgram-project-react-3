from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from recipes.models import Recipe, Tag, Ingredient, Favorite
from users.models import User
from .serializers import (RecipeSerializer, IngredientSerializer,
                          CustomUserSerializer,
                          TagSerializer, FavoriteSerializer)


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = IngredientSerializer


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = TagSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = FavoriteSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
