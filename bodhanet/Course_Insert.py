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

class Course_Insert:
	def create_new_lecture(self, lecture_section, lecture_name, lecture_description, lecture_video):
		course_section = Course_Sections.objects.get(course_section_name=lecture_section)
		lecture=Course_Lecture_Details(lecture_course_subsection=course_section, lecture_name=lecture_name, lecture_description=lecture_description, lecture_video=lecture_video)
		lecture.save()
		
	def create_new_course_section(self, new_course_section, course_id):
		course=Course_Details.objects.get(id=course_id)
		course_section=Course_Sections(course_section_name=new_course_section, course=course)
		course_section.save()		
