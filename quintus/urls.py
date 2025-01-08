
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap

sitemaps = {
    "static": StaticViewSitemap,
    'blog': BlogSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls', namespace='website')),
    path('blog/',include('blog.urls', namespace = 'blog')),
    path('accounts/',include('accounts.urls' , namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)