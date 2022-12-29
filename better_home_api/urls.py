from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

from decorator_include import decorator_include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from admin_module.views import login_admin

schema_view = get_schema_view(
   openapi.Info(
      title="Better Home APIs",
      default_version='v1',
      description="Better home API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="general.sina.amini.20@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', decorator_include(login_required, include('admin_module.urls')), name='admin'),
    path('admin/login/', login_admin, name='login-admin'),
    path('api/v1/', include('api_v1_module.urls'), name='api-v1'),
    path('docs', schema_view.with_ui('redoc', cache_timeout=0), name='docs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
