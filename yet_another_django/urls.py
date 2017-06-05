from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from core.views import JResponseView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^json1/$', JResponseView.as_view(), {'range_1st': range(1, 11), 'range_2nd': range(31, 41)}, name='get_j1'),
    url(r'^json2/$', JResponseView.as_view(), {'range_1st': range(1, 21), 'range_2nd': range(41, 51)}, name='get_j2'),
    url(r'^json3/$', JResponseView.as_view(), {'range_1st': range(1, 31), 'range_2nd': range(51, 61)}, name='get_j3'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
