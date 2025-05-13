from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import car_viw, new_car_viw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', car_viw, name='cars_list'),
    path('new_car/', new_car_viw, name='new_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
