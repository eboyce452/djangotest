from django import template

register = template.Library()

#@register.filter(name = 'filtername')
#def example(value,arg):
    #Do something to value based on arg here#
    ##Ex. return value.replace(arg,'')##
    #return value