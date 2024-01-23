from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from home.views import set_language


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cked/', include('cked.urls')),
    path('', include('home.urls'))
]


urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("language/<str:language>", set_language, name="set-language"),
]
