from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from .models import Category, Actor, Genre, Cinema, CinemaFrame, RatingStar, Rating, Reviews

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CinemaAdminForm(forms.ModelForm):
    descriptions = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Cinema
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'get_image', ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', ]


class ReviewAdminInLine(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ('name', 'email')


class CinemaFrameAdmin(admin.TabularInline):
    model = CinemaFrame
    extra = 0

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['title', "get_image", 'year', 'country', 'budget', 'category', 'url', 'draft']
    inlines = [CinemaFrameAdmin, ReviewAdminInLine]
    list_editable = ('draft',)
    save_on_top = True
    save_as = True
    readonly_fields = ('get_image',)
    form = CinemaAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="120"')

    get_image.short_description = 'Постер'


@admin.register(CinemaFrame)
class CinemaFrameAdmin(admin.ModelAdmin):
    list_display = ['title', 'cinema', 'get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width ="50" height="50"')


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ['value', ]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['ip', 'star', 'cinema']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'parent', 'cinema']
    readonly_fields = ('name', 'email')
