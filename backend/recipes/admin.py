from django.contrib import admin

from .models import (FavoriteRecipe, Ingredient, IngredientToRecipe, Recipe,
                     Basket, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'colour')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


@admin.register(IngredientToRecipe)
class IngredientToRecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('name', 'author', 'tag')
    readonly_fields = ('count_favorites',)

    def count_favorites(self, obj):
        return obj.favorites.count()


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass