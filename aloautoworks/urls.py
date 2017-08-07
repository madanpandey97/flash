
from django.conf.urls import url
from . import views
app_name='aloautoworks'

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'appointments/$', views.appointment_book, name='appointment'),
    url(r'services_aloautoworks/$', views.services, name='services_alo'),
    url(r'blogs_aloautoworks/$', views.blogs, name='blogs_alo'),
    url(r'blog_detail_aloautoworks/$', views.blog_detail, name='blog_detail_alo'),
    url(r'contact_aloautoworks/$', views.contact, name='contact_alo'),
    url(r'contact/$', views.checkcontact, name='xxcontact_alo'),
    url(r'thanks/$', views.thanks, name='thank'),

   


    ]