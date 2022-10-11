from django import template
from cinema.models import Category, Cinema

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('cinema/tags/last_cinema.html')
def get_last_cinema():
    cinema = Cinema.objects.order_by('-id')[:5]
    return {'last_cinema': cinema}
