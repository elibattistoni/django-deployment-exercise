from django import template

# register this script
register = template.Library()

# my custom function filters
#@register.filter(name="cut") # it should be this or register.filter(...) after the function
def cut(value,arg):
    """This cuts out all the values of 'arg' from the string

    Args:
        value (_type_): _description_
        arg (_type_): _description_
    """
    return value.replace(arg,"")

# register the filter
register.filter("cut",cut)
# first parameter: then name you want to use in the html to refer to this filter;
# second parameter: the function itself

@register.filter(name="slice")
def slice(value,arg):
    if arg <= len(value):
        value = value[:arg]
    return value
