from django.urls import path # Como este es un archivo creado por mi, yo mismo pongo la importación
from funciones import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.home_page, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)