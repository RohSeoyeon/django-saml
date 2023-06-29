from django.urls import path
from django.contrib import admin
from .views import attrs, index, metadata, TestAPIView, TempAPIView

admin.autodiscover()

urlpatterns = [
    path('', index, name='index'),
    path('attrs/', attrs, name='attrs'),
    path('metadata/', metadata, name='metadata'),
    path('test', TestAPIView.as_view(), name='test'),
]
