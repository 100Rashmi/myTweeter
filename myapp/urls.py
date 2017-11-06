from myapp import views as myapp_views
from django.conf.urls import url


urlpatterns = [
    url(r'^signup', myapp_views.signup_submit, name='signup'),
    url(r'^login', myapp_views.login_submit, name='login'),
    url(r'^dweet', myapp_views.dweet, name='dweet'),
    url(r'^like', myapp_views.like, name='like'),
    url(r'^comment', myapp_views.comment, name='comment'),
    url(r'^follow', myapp_views.follow, name='follow'),
    url(r'^feed', myapp_views.feed, name='feed'),
    url(r'^searchDweet', myapp_views.searchDweet, name='searchDweet'),
    url(r'^searchUsers', myapp_views.searchDweeter, name='searchUsers'),

]