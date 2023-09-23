from django.contrib import admin
# include helps us connect with the urls.py file in thewcwebpage app or any other app
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # summernote added for thewcwebpage app text editor
    path('summernote/', include('django_summernote.urls')),
    path('', include('thewcwebpage.urls'), name='thewcwebpage_urls'),
    # allauth added for thewcwebpage app to manage user accounts
    path('accounts/', include('allauth.urls')),
]
