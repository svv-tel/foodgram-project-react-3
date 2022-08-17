from django.contrib import admin
from .models import (
    Recipe, Ingredient, Tag, IngredientToRecipe,
    FavoriteRecipe, Basket
)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'name',)
    search_fields = ('name',)
    list_filter = ('author', 'name', 'tag')
    empty_value_display = '-пусто-'

    def count_favorites(self, obj):
        return obj.favorites.count()


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'measurement_unit',)
    list_filter = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'colour', 'slug')
    list_filter = ('name',)


class IngredientToRecipeAdmin(admin.ModelAdmin):
    pass


class FavoriteRecipeAdmin(admin.ModelAdmin):
    pass


class BasketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(IngredientToRecipe, IngredientToRecipeAdmin)
admin.site.register(FavoriteRecipe, FavoriteRecipeAdmin)
admin.site.register(Basket, BasketAdmin)
