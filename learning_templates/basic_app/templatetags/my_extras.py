from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """ 
    this cuts all vuls of arg from strinng
    """

    return value.replace(arg, '')


# register.filter('cut', cut)
