from django.conf.urls.static import static
from django.urls import path
import mainapp.views as mainapp
from geekshop import settings


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),
    path('<int:pk>/', mainapp.products, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
