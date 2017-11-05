from myapp import views as myapp_views
from django.conf.urls import url


urlpatterns = [
    url(r'^hello', myapp_views.hello, name='hello'),
    url(r'^signup_submit', myapp_views.signup_submit, name='signup_submit'),
    url(r'^login_submit', myapp_views.login_submit, name='login_submit'),
    url(r'^dweet', myapp_views.dweet, name='dweet'),
    url(r'^like', myapp_views.like, name='like'),
    url(r'^comment', myapp_views.comment, name='comment'),
    url(r'^follow', myapp_views.follow, name='follow'),


]