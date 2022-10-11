from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('Категория', max_length=150)
    descriptions = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    """ Actor and Producer"""
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    descriptions = models.TextField('Описание')
    image = models.ImageField('Фотография', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер и режессеры'
        verbose_name_plural = 'Актеры и режессеры'


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=150)
    descriptions = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Cinema(models.Model):
    title = models.CharField('Название', max_length=150)
    tagline = models.CharField('Слоган', max_length=150, default='')
    descriptions = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='poster/')
    year = models.PositiveSmallIntegerField('Год', default=2022)
    country = models.CharField('Страна', max_length=50)
    world_premiere = models.DateField('Примьера в мире', default=timezone.now)
    budget = models.PositiveSmallIntegerField('Бюджет', default=0, help_text="Указывать в $")
    fees_in_usa = models.PositiveSmallIntegerField('Сборы в США', default=0, help_text="Указывать в $")
    fees_in_world = models.PositiveSmallIntegerField('Сборы в мире', default=0, help_text="Указывать в $")
    producer = models.ManyToManyField(
        Actor,
        verbose_name='Режиссер',
        related_name='film_producer'
    )
    actors = models.ManyToManyField(
        Actor,
        verbose_name='Актеры',
        related_name='film_actor'
    )
    genres = models.ManyToManyField(
        Genre,
        verbose_name='Жанры'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True
    )
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cinema_detail', kwargs={'slug': self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class CinemaFrame(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    descriptions = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='cinema_frame/')
    cinema = models.ForeignKey(
        Cinema,
        verbose_name='Фильм',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    ip = models.CharField('IP адресс', max_length=20)
    star = models.ForeignKey(
        RatingStar,
        verbose_name='Звезда',
        on_delete=models.CASCADE
    )
    cinema = models.ForeignKey(
        Cinema,
        verbose_name='Фильм',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.star}-{self.cinema}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    message = models.TextField()
    parent = models.ForeignKey(
        'self',
        verbose_name='Родитель',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    cinema = models.ForeignKey(
        Cinema,
        verbose_name='Фильм',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}-{self.cinema}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
