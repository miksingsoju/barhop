from django import template

register = template.Library()


@register.filter(name="subtractAB")
def subtractAB(value, arg2):
    return int(value) - int(arg2)


@register.filter(name="subtractBA")
def subtractBA(value, arg2):
    return int(arg2) - int(value)
