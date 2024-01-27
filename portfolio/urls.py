from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from home.views import set_language


urlpatterns = [
    path('admin/', admin.site.urls),
    path("language/<str:language>", set_language, name="set-language"),
    path('', include('home.urls')),
    path('tinymce/', include('tinymce.urls')),

]


urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

