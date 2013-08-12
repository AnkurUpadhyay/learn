#import statements
from models import User
from models import Course_Details
from models import Course_Categories
from models import User_Course_Details
from models import Course_Lecture_Details
from models import Lecture_Question_Details
from models import Question_Answer_Details
from models import Answer_Comment_Details
from models import Course_Sections
from Insert_Into_Database import Insert_Into_Database
from Fetch_From_Database import Fetch_From_Database

class Course_Fetch:
	def fetch_course(self, course_id):
		course=Course_Details.objects.get(id=course_id)
		return course
		
	def fetch_course_creator(self, course_id):
		course=Course_Details.objects.get(id=course_id)
		return course.course_created_by
		
	def fetch_course_category(self, course_id):
		course=Course_Details.objects.get(id=course_id)
		return course.course_category

	def fetch_course_lectures(self, course_id):
		course=Course_Details.objects.get(id=course_id)
		course_sections=course.course_sections_set.all()
		course_lectures={}
		for course_section in course_sections:
			section_lectures=course_section.course_lecture_details_set.all()
			course_lectures[course_section.course_section_name]=section_lectures
		return course_lectures
		
	def fetch_lecture_problems(self, lecture_id):
		lecture=Course_Lecture_Details(id=lecture_id)
		problem_set=lecture.lecture_problems_set.all()
		return problem_set
		
	def fetch_problem_choices(self, problem_id):
		problem=Lecture_Problems(id=problem_id)
		choice_set=problem.problem_choice_set.all()
		return choice_set
		
	def fetch_correct_choice_set(self, problem_id):
		problem=Lecture_Problems(id=problem_id)
		correct_choice_set=problem.problem_solutions_set.all()
		return correct_choice_set
		
	def fetch_course_sections(self, course_id):
		course=Course_Details.objects.get(id=course_id)
		course_sections=course.course_sections_set.all()
		return course_sections
