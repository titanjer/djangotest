from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^view/', views.multi_input_view),
)
