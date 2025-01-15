
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.conf.urls import handler404, handler403, handler400, handler500
from . import error_views
from blog import views

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

    path('robots.txt', views.robots_txt),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Set custom error handlers
handler404 = error_views.handler404
handler403 = error_views.handler403
handler400 = error_views.handler400
handler500 = error_views.handler500