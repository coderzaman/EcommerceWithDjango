from django.contrib import admin
from django.urls import path, include

# To Show Media File
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ShopApp.urls')),
    path('account/', include('LoginApp.urls')),
    path('shop/', include('OrderApp.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)