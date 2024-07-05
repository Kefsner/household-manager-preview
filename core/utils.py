from base.views import BaseView
from django.http import HttpRequest

def next_page(request: HttpRequest) -> tuple[str, dict]:
    url = request.POST.get('url').split('/')[3]
    if url == 'accounts':
        return 'accounts:home'
    elif url == 'categories':
        return 'categories:home'
    elif url == 'creditcards':
        return 'creditcards:home'
    elif url == 'users':
        return 'users:home'
    else:
        return 'base:home'