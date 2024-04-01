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
        imgSrc = '/static/assets/icons/supscription.svg'
    elif category.lower() == 'hobbies':
        imgSrc = '/static/assets/icons/ocio.svg'
    elif category.lower() == 'medication':
        imgSrc = '/static/assets/icons/medication.svg'
    else:
        imgSrc = '/static/assets/icons/Various.svg'

    
    print(imgSrc)
    
    return {'src': imgSrc}


@register.inclusion_tag('partials/optionals.html')
def render_optional():
    subscriptions = [
        {
            'name': 'Netflix',
            'url': '/static/assets/subscription/netflix.svg' 
        },
        {
            'name': 'Spotify',
            'url': '/static/assets/subscription/spotify.svg'
        },
        {
            'name': 'amazon',
            'url': '/static/assets/subscription/amazon.svg'
        },
        {
            'name': 'google',
            'url': '/static/assets/subscription/google.svg'
        },
        {
            'name': 'facebok',
            'url': '/static/assets/subscription/facebook.svg'
        }
    ]

    return {'subscriptions': subscriptions}