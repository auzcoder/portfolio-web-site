from django.shortcuts import render
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from tajriba.models import Tajriba
from talim.models import Talim
from loyiha.models import Loyiha
from sertifikat.models import Sertifikat
from maqola.models import Maqola
from aloqa.models import About


def set_language(request, language):
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

    tajriba = Tajriba.objects.all().order_by('-created_at' and 'ended_at')
    talim = Talim.objects.all().order_by('-created_at' and 'ended_at')
    loyiha = Loyiha.objects.all().order_by('-created_at')[:3]
    sertifikat = Sertifikat.objects.filter(is_active=True).order_by('-created_at')[:3]
    maqola = Maqola.objects.filter(is_active=True).order_by('-created_at')[:3]
    about = About.objects.all().order_by('-created_at')[:1]

    context = {
        'tajriba': tajriba,
        'talim': talim,
        'loyiha': loyiha,
        'sertifikat': sertifikat,
        'maqola': maqola,
        'about': about,
    }

    return render(request, 'core/index.html', context)




