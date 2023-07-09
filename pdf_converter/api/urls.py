from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('excel/',Excelfiles.as_view()),
    path('student/',studentapi.as_view()),
    path('get_book/',get_book),
    #path("genric-student/",studentGenric.as_view()),
    #path("genric-student2/<name>/",studentGenric2.as_view()),
    path('pdf/',GeneratePdf.as_view()),

]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()