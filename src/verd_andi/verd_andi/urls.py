"""
    verd_andi URL Configuration

    # The `urlpatterns` list routes URLs to views.
    # For more information please see:
    #     https://docs.djangoproject.com/en/1.10/topics/http/urls/
    # Examples:
    # Function views
    #     1. Add an import:  from my_app import views
    #     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
    # Class-based views
    #     1. Add an import:  from other_app.views import Home
    #     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
    # Including another URLconf
    #     1. Import the include() function:
    #        from django.conf.urls import url, include
    #     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin


from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/survey/udash/'), name='index'),
    # url(r'^$', home, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^survey/', include('survey.urls')),
    # url(r'^export_action/', include(
    #    "export_action.urls", namespace="export_action")),
]


if settings.DEBUG:
    urlpatterns += static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
