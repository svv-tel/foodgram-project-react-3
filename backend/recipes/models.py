from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название тега', unique=True,
        max_length=200
    )
    colour = models.CharField(
        verbose_name='Цвет в HEX', unique=True,
        max_length=7
    )
    slug = models.SlugField(unique=True, max_length=200)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название ингредиента', unique=True,
        max_length=100
    )
    measurement_unit = models.CharField(
        verbose_name='Параметр измерения ингредиента', unique=True,
        max_length=100
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    '''Модель рецепта'''
    author = models.ForeignKey(
        User, verbose_name='Автор рецепта',
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    name = models.CharField(verbose_name='Название рецепта', max_length=200)
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='recipes/',
        blank=True,
        null=True,
    )
    text = models.TextField(verbose_name='Описание рецепта', )
    ingridient = models.ManyToManyField(Ingredient,
                                        verbose_name='Ингридиенты рецепта', )
    tag = models.ManyToManyField(Tag, verbose_name='Теги рецепта', )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления по рецепту',
        validators=[
            MinValueValidator(1, 'Не может быть  меньше минуты.')
        ]
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name


class IngredientToRecipe(models.Model):
    """Модель для связи ингридиентов и рецепта"""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_total',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredients_total',
        verbose_name='Ингредиент',
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Количество',
        validators=[
            MinValueValidator(1, 'Минимальное количество ингредиента - 1')
        ]
    )

    class Meta:
        verbose_name = 'Ингредиент для рецепта'
        verbose_name_plural = 'Ингредиенты для рецепта'
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_ingredient'
            )
        ]

    def __str__(self):
        return self.ingredient


class FavoriteRecipe(models.Model):
    """Модель добавления избранного рецепта"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_user_recipe'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.recipe.name}'


class Basket(models.Model):
    """Модель добавления корзину покупок"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_cart_user'
            )
        ]
