from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import car_viw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', car_viw),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
