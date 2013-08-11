# import statements
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from User.Insert_Into_Database import Insert_Into_Database
from User.Fetch_From_Database import Fetch_From_Database
from Course.Course_Fetch import Course_Fetch
from Course.Course_Insert import Course_Insert
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from django import http
from django.core import serializers
import json
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

def home(request, user_id):
	fetch=Fetch_From_Database()
	course_created_list=fetch.fetch_created_courses(user_id)
	maximum_created_course_id=course_created_list[0].id
	context={'user_id': user_id, 'course_created_list': course_created_list, 'maximum_created_course_id': maximum_created_course_id}
	return render(request, 'tutors/home.html', context)
	
def course_home(request, course_id):
	course_requested=Course_Fetch()
	course=course_requested.fetch_course(course_id)
	course_creator=course_requested.fetch_course_creator(course_id)
	course_lectures=course_requested.fetch_course_lectures(course_id)
	context={'course': course, 'course_lectures': course_lectures}
	return render(request, 'tutors/course.html', context)

def create_new_course(request, user_id):
	insert=Insert_Into_Database()
	course_name=request.POST['course_name']
	course_description=request.POST['course_description']
	course_category=request.POST['course_category']
	course_introduction_video=request.FILES['course_introduction_video']
	insert.create_new_course(course_created_by=user_id, course_name=course_name, course_category_name=course_category, course_description=course_description, course_introduction_video=course_introduction_video)
	return HttpResponseRedirect(reverse('tutors:home', args=[user_id]))
	
def create_new_lecture(request, course_id):
	course_insert=Course_Insert()
	lecture_name=request.POST['lecture_name']
	lecture_description=request.POST['lecture_description']
	lecture_section=request.POST['lecture_section']
	new_course_section=request.POST['new_course_section']
	lecture_video=request.FILES['lecture_video']
	if new_course_section:
		print("user creating new course section::"+new_course_section)
		course_insert.create_new_course_section(new_course_section=new_course_section, course_id=course_id)
		course_insert.create_new_lecture(lecture_section=new_course_section, lecture_name=lecture_name, lecture_description=lecture_description, lecture_video=lecture_video)
	else:
		print("user uploading lecture in existing course section")
		course_insert.create_new_lecture(lecture_section=lecture_section, lecture_name=lecture_name, lecture_description=lecture_description, lecture_video=lecture_video)
	return HttpResponseRedirect(reverse('tutors:course_home', args=[course_id]))
			
def fetch_course_categories(request):
	fetch=Fetch_From_Database()
	course_categories=fetch.fetch_course_categories()
	categories=serializers.serialize("json", course_categories)
	return http.HttpResponse(categories, mimetype=u'application/javascript')
	
def fetch_course_sections(request, course_id):
	print("fetching course sections")
	course_fetch=Course_Fetch()
	course_section_list=course_fetch.fetch_course_sections(course_id)
	sections=serializers.serialize("json", course_section_list)
	print(sections)
	return http.HttpResponse(sections, mimetype=u'application/javascript')
