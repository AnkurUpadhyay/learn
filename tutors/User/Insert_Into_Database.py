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

class Insert_Into_Database:
	def register_new_user(self, user_name, user_email):
		user=User(user_name=user_name, user_email=user_email)
		user.save()
		
	def create_new_course(self, course_created_by, course_name, course_category_name, course_description,course_introduction_video):
		course_category=Course_Categories.objects.get(course_category_name=course_category_name)
		user=User.objects.get(id=course_created_by)
		course=Course_Details(course_name=course_name, course_created_by=user, course_description=course_description, course_category=course_category, course_introduction_video=course_introduction_video)
		course.save()
		
	def register_for_course(self, course, registered_user):
		course=Course_Details.objects.get(id=course)
		registered_user=User.objects.get(id=user)
		course_member=User_Course_Details(user=registered_user, user_course=course)
		course_member.save()
		
	def upload_new_lecture(self, course, lecture_name, lecture_description):
		course=Course_Details.objects.get(id=course)
		lecture=Course_Lecture_Details(course=course, lecture_name=lecture_name, lecture_description=lecture_description)
		lecture.save()
		
	def ask_question(self, lecture, question_asked_by_user, question_text):
		user = User.objects.get(id=question_asked_by_user)
		lecture=Course_Lecture_Details(id=lecture)
		question=Lecture_Question_Details(lecture=lecture, question_asked_by_user=user, question_text=question_text)
		question.save()
		
	def answer_question(self, question, question_answered_by_user, answer_text):
		user=User.objects.get(id=question_asked_by_user)
		question=Lecture_Question_Details.objects.get(id=question)
		answer=Question_Answer_Details(answer_for_question=question, answered_by_user=user, answer_text=answer_text)
		answer.save()
		
	def upvote_question(self, question, user_upvoted):
		question=Lecture_Question_Details.objects.get(id=question)
		user=User.objects.get(id=user_upvoted)
		question_upvote = Question_Upvotes(question=question, user_upvoted=user)
		question_upvote.save()
		
	def follow_User(self, user_followed, user_followed_by):
		user_followed=User.objects.get(id=user_followed)
		user_followed_by=User.objects.get(id=user_followed_by)
		user_follow=User_Followers(user_followed=user_followed, user_followed_by=user_followed_by)
		user_follow.save()
		
	def upvote_answer(self, answer, user_upvoted):
		answer=Question_Answer_Details.objects.get(id=answer)
		user=User.objects.get(id=user_upvoted)
		answer_upvote=Answer_Upvotes(answer=answer, user_upvoted=user)
		answer_upvote.save()
		
	def comment_answer(self, answer, commented_by_user, comment_text):
		user=User.object.get(id=commented_by_user)
		answer=Question_Answer_Details.objects.get(id=answer)
		comment=Answer_Comment_Details(comment_for_answer=answer, commented_by_user=user, comment_text=comment_text)
		comment.save() 
