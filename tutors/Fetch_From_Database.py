#import statements
import sys
from models import User
from models import Course_Details
from models import Course_Categories
from models import User_Course_Details
from models import Course_Lecture_Details
from models import Lecture_Question_Details
from models import Question_Answer_Details
from models import Answer_Comment_Details

class Fetch_From_Database:
	def fetch_created_courses(self, user_id):
		user=User.objects.get(id=user_id)
		user_created_course=user.course_details_set.all().order_by('-id')
		return user_created_course

	def fetch_course_lectures(self, course):
		course=Course_Details(id=course)
		lecture_list=Course_Lecture_Details(course=course)
		return lecture_list
		
	def course_users(self, course):
		course=Course_Details(course=course)
		users_list=User_Course_Details(course=course)
		return user_list
		
	def fetch_course_categories(self):
		course_categories=Course_Categories.objects.all()
		return course_categories		
