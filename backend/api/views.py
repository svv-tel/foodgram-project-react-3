from djoser.views import UserViewSet
from rest_framework import viewsets, mixins
from recipes.models import Recipe, Tag, Ingredient, Favorite
from rest_framework.permissions import AllowAny
from users.models import User
from .serializers import (RecipeSerializer, IngredientSerializer,
                          CustomUserSerializer,
                          TagSerializer, FavoriteSerializer)


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class RetrieveListViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    pass


class TagsViewSet(RetrieveListViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
