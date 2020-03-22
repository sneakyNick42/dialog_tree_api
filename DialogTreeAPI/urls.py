"""DialogTreeAPI URL Configuration."""

from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='DialogTree API', description='API')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('apps.users.urls')),
    path('', include('apps.dialog_tree.urls')),
]
