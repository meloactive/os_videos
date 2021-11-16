from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 

from .views import demo_view
from . import views

urlpatterns = [
	# Demo view
	path('', demo_view, name='demo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)