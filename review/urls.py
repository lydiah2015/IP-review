from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
     url('^$',views.posts,name='posts'),
     url(r"^accounts/profile/$", views.my_profile, name = "my_profile"),
     # url(r"^profile/update/$", views.update_profile, name = "update_profile"),
     
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)