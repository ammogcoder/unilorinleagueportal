from django.conf.urls import url
from . import views
from .views import CreateView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns= [
	url(r'^posts/$', CreateView.as_view(), name="posts")

	]
	
urlpatterns = format_suffix_patterns(urlpatterns)