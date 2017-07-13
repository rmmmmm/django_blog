from django.conf.urls import url
import blog.views

urlpatterns = [
    url(r'^1/$', blog.views.myresp,name='aaaaaa'),
]
