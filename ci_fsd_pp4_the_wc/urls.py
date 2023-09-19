from django.contrib import admin
from django.urls import path, include  # include added for thewcwebpage app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),  # summernote added for thewcwebpage app
    path('', include('thewcwebpage.urls'), name='thewcwebpage_urls'),
    path('accounts/', include('allauth.urls')),  # allauth added for thewcwebpage app
]
