"""innocation_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from core.utlis import admin_setup


admin.site.site_header = 'Innovation Management System'

admin.site.index_title = 'Administration'

admin_setup.site_header = 'Innovation Management System'

admin_setup.index_title = 'Setup'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin-setup/', admin_setup.urls),
]
urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
