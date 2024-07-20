from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('siteui.urls')),
    path('posts/', include('post.urls')),
    # url name 'posts' it a name whatever you want
]

#necessary if you use old version django
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
