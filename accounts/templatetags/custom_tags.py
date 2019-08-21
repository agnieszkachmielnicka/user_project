from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def if_allowed(value):
    age = timezone.now().year - value.year
    if age > 13:
        return "allowed"
    return "blocked"


@register.filter
def if_bizzfuzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return "BizzFuzz"
    elif value % 3 == 0:
        return "Bizz"
    elif value % 5 == 0:
        return "Fuzz"
    else:
        return value
