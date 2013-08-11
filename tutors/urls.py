from django.conf.urls import patterns, url

from tutors import views

urlpatterns = patterns('',
	url(r'^(?P<user_id>\d+)/$', views.home, name='home'),
	url(r'^fetch_course_categories/$', views.fetch_course_categories, name='fetch_course_categories'),
	url(r'^(?P<user_id>\d+)/create_new_course/$', views.create_new_course, name='create_new_course'),
	url(r'^course_home/(?P<course_id>\d+)/$', views.course_home, name='course_home'),
	url(r'^(?P<course_id>\d+)/fetch_course_sections/$', views.fetch_course_sections, name='fetch_course_sections'),
	url(r'^(?P<course_id>\d+)/create_new_lecture/$', views.create_new_lecture, name='create_new_lecture'),
)
