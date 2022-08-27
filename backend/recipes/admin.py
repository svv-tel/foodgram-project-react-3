from django.contrib import admin
from django.db.models import Sum, Count

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag, )

EMPTY_VALUE = '<-EMPTY->'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag model representation in admin panel"""
    list_display = ('id', 'name', 'color', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


class IngredientRecipeInline(admin.TabularInline):
    """IngredientRecipe model representation in admin panel"""
    model = IngredientRecipe


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Ingredient model representation in admin panel"""
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Recipe model representation in admin panel"""
    list_display = ('id', 'name', 'author')
    search_fields = ('author', 'name', 'tags')
    list_filter = ('author', 'name', 'tags')
    inlines = (IngredientRecipeInline,)
    empty_value_display = EMPTY_VALUE

    def is_favorited(self, obj):
        return obj.favorite_recipe.count()


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Favorite model representation in admin panel"""
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = EMPTY_VALUE


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """ShoppingCart model representation in admin panel"""
    list_display = ('user', 'get_recipe', 'count_ingredients')
    empty_value_display = EMPTY_VALUE

    def get_recipe(self, obj):
        return [f'{item["name"]} ' for item in obj.recipe.values('name')[:5]]

    def count_ingredients(self, obj):
        return (
            obj.recipe.all().annotate(count_ingredients=Count('ingredients'))
                .aggregate(total=Sum('count_ingredients'))['total']
        )


class IngredientRecipeAdmin(admin.ModelAdmin):
    """Ingredients in recipe model representation in admin panel"""
    list_display = ('ingredient', 'recipe', 'amount')
    list_filter = ('ingredient', 'recipe', 'amount')
