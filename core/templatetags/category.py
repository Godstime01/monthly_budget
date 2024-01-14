from django import template

register = template.Library()

@register.simple_tag
def category_icon(category):

    imgSrc = ''
    if category.lower() == 'debt':
        imgSrc = '/static/assets/icons/debts.svg'
    elif category.lower() == 'food':
        imgSrc = '/static/assets/icons/food.svg'
    elif category.lower() == 'rent':
        imgSrc = '/static/assets/icons/rent.svg'
    elif category.lower() == 'saving':
        imgSrc = '/static/assets/icons/saving.svg'
    elif category.lower() == 'subscription':
        imgSrc = '/static/assets/icons/subscription.svg'
    elif category.lower() == 'hobbies':
        imgSrc = '/static/assets/icons/ocio.svg'
    elif category.lower() == 'medication':
        imgSrc = '/static/assets/icons/medication.svg'

    
    print(imgSrc)
    
    return {'src': imgSrc}