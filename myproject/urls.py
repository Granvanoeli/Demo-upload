# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin # UNCOMMENT THIS LINE
admin.autodiscover() # UNCOMMENT THIS LINE, TOO!


urlpatterns = patterns('',
	url(r'^myapp/', include('myproject.myapp.urls')),
	url(r'^$', RedirectView.as_view(url='/myapp/list/')), # Just for ease of use.
    url(r'^admin/', include(admin.site.urls)), # ADD THIS LINE

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
