from django.contrib import admin
# include helps us connect with the urls.py file in thewcwebpage app or any other app
from django.urls import path, include
# static and settings added for thewcwebpage app -summernote-
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # summernote added for thewcwebpage app text editor
    path('summernote/', include('django_summernote.urls')),
    path('', include('thewcwebpage.urls'), name='thewcwebpage_urls'),
    # allauth added for thewcwebpage app to manage user accounts
    path('accounts/', include('allauth.urls')),
]
# static and settings added for thewcwebpage app -summernote-
# If in DEBUG mode, we will serve the media files through Django
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
