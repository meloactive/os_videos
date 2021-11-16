from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 

from .views import demo_view, test_js, test_js_html, post_add
# from . import views

urlpatterns = [
	# Demo view
	path('', demo_view, name='demo'),
	path('test_js', test_js, name='test_js'),
	path('test_js_html', test_js_html, name='test_js_html'),
	path('add', post_add, name='add'),
	# test_js_html
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)