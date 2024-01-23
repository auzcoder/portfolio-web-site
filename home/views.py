from django.shortcuts import render
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from tajriba.models import Tajriba


def set_languages(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response


def homepage(request):

    tajriba = Tajriba.objects.filter(is_active=True).order_by('-created_at' and 'started_at')
    tajriba_old = Tajriba.objects.filter(is_active=False).order_by('-created_at' and 'started_at' and '-ended_at')

    context = {
        'tajriba': tajriba,
        'tajriba_old': tajriba_old,
    }

    return render(request, 'core/index.html', context)




