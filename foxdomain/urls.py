from django.conf.urls import include, url
from django.contrib import admin
import domains.urls

urlpatterns = [
    url(r'^domain/', view=include(domains.urls.urlpatterns, namespace='Domain')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_docs.urls')),
]