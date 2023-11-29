from . import views

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('file/', views.file_upload, name='file_upload'),
    path('file/list/', views.file_list, name='file_list'),
    path('page/<int:id>/<int:page_number>/', views.page_reader, name='page_reader')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
