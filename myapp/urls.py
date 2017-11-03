from myapp import views as myapp_views
from django.conf.urls import url


urlpatterns = [
    url(r'^hello/', myapp_views.hello, name='hello'),
    url(r'^morning/', myapp_views.morning, name='morning'),

]