from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from quiz.urls import router as quiz_router

VERSION = "v1"
PREFIX = "api"
API_PREFIX = f"{PREFIX}/{VERSION}"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_PREFIX}/quiz/', include(quiz_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
