# Generated by Django 4.1.2 on 2022-10-08 21:18

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Актер и режессеры',
                'verbose_name_plural': 'Актеры и режессеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('tagline', models.CharField(default='', max_length=150, verbose_name='Слоган')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='poster/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2022, verbose_name='Год')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('world_premiere', models.DateField(default=django.utils.timezone.now, verbose_name='Примьера в мире')),
                ('budget', models.PositiveSmallIntegerField(default=0, help_text='Указывать в $', verbose_name='Бюджет')),
                ('fees_in_usa', models.PositiveSmallIntegerField(default=0, help_text='Указывать в $', verbose_name='Сборы в США')),
                ('fees_in_world', models.PositiveSmallIntegerField(default=0, help_text='Указывать в $', verbose_name='Сборы в мире')),
                ('url', models.SlugField(max_length=150, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='cinema.actor', verbose_name='Актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Жанр')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema', verbose_name='Фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, verbose_name='IP адресс')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='cinema.cinema', verbose_name='Фильм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.ratingstar', verbose_name='Звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='CinemaFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='cinema_frame/', verbose_name='Изображение')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Кадр из фильма',
                'verbose_name_plural': 'Кадры из фильма',
            },
        ),
        migrations.AddField(
            model_name='cinema',
            name='genres',
            field=models.ManyToManyField(to='cinema.genre', verbose_name='Жанры'),
        ),
        migrations.AddField(
            model_name='cinema',
            name='producer',
            field=models.ManyToManyField(related_name='film_producer', to='cinema.actor', verbose_name='Режиссер'),
        ),
    ]