from django.db import models

# Create your models here.

class User(models.Model):
	user_name=models.CharField(max_length=200)
	user_email = models.CharField(max_length=200)
	def __unicode__(self):
		return self.user_name
		
class Course_Categories(models.Model):
	course_category_name=models.CharField(max_length=200)
	def __unicode__(self):
		return course_category

def course_introduction_file_name(instance, filename):
	return '/home/ankur/Documents/lecture-intro'.join(['content', instance.id, filename])

class Course_Details(models.Model):
	course_name = models.CharField(max_length=200)
	course_created_by = models.ForeignKey(User)
	course_description = models.CharField(max_length=500)
	course_category = models.ForeignKey(Course_Categories)
	course_introduction_video = models.FileField(upload_to="/home/ankur/")
	def __unicode__(self):
		return self.course_name
		
class User_Course_Details(models.Model):
	user = models.ForeignKey(User)
	user_course = models.ForeignKey(Course_Details)
	def __unicode__(self):
		return self
		
class User_Followers(models.Model):
	user = models.ForeignKey(User, related_name = "user_id_followed")
	user_follower = models.ForeignKey(User, related_name = "user_id_followed_by")
	def __unicode__(self):
		return self
		
class Course_Sections(models.Model):
	course_section_name=models.CharField(max_length=500)
	course=models.ForeignKey(Course_Details)
	def __unicode__(self):
		return self.course_section_name
		
class Course_Lecture_Details(models.Model):
	lecture_course_subsection=models.ForeignKey(Course_Sections)
	lecture_name = models.CharField(max_length=200)
	lecture_description = models.CharField(max_length=500)
	lecture_video = models.FileField(upload_to="/home/ankur/")
	def __unicode__(self):
		return self.lecture_name
	
class Lecture_Question_Details(models.Model):
	lecture = models.ForeignKey(Course_Lecture_Details)
	question_asked_by_user = models.ForeignKey(User)
	question_text = models.CharField(max_length=500)
	def __unicode__(self):
		return self.question_text
	
class Question_Answer_Details(models.Model):
	answer_for_question = models.ForeignKey(Lecture_Question_Details)
	answered_by_user = models.ForeignKey(User)
	answer_text = models.CharField(max_length=500)
	def __unicode__(self):
		return self.answer_text
		
class Question_Upvotes(models.Model):
	question = models.ForeignKey(Lecture_Question_Details)
	user_upvoted = models.ForeignKey(User)
	def __unicode__(self):
		return self
		
class Answer_Upvotes(models.Model):
	answer = models.ForeignKey(Question_Answer_Details)
	user_upvoted = models.ForeignKey(User)
	def __unicode__(self):
		return self
	
class Answer_Comment_Details(models.Model):
	comment_for_answer = models.ForeignKey(Question_Answer_Details)
	commented_by_user = models.ForeignKey(User)
	comment_text = models.CharField(max_length=500)
	def __unicode__(self):
		return self.comment_text
		
class Course_Problemset(models.Model):
	course=models.ForeignKey(Course_Details)
	problemset_name=models.CharField(max_length=500)
	problemset_description=models.CharField(max_length=1000)
	def __unicode__(self):
		return self.problemset_name
		
class Problemset_Problems(models.Model):
	problemset=models.ForeignKey(Course_Problemset)
	problem_text=models.CharField(max_length=1000)
	def __unicode__(self):
		return self.problem_text
		
class Problemset_Problem_Choices(models.Model):
	problem=models.ForeignKey(Problemset_Problems)
	choice_text=models.CharField(max_length=1000)
	def __unicode__(self):
		return self.choice_text	

class Problemset_Problem_Solutions(models.Model):
	problem=models.ForeignKey(Problemset_Problems)
	correct_choice=models.ForeignKey(Problemset_Problem_Choices)
	def __unicode__(self):
		return self

class Lecture_Quiz(models.Model):
	lecture=models.ForeignKey(Course_Lecture_Details)
	quiz_name=models.CharField(max_length=500)
	quiz_description=models.CharField(max_length=1000)
	def __unicode__(self):
		return self.quiz_name
		
class Quiz_Problems(models.Model):
	quiz=models.ForeignKey(Lecture_Quiz)
	problem_text=models.CharField(max_length=1000)
	def __unicode__(self):
		return self.problem_text
		
class Quiz_Problem_Choices(models.Model):
	problem=models.ForeignKey(Quiz_Problems)
	choice_text=models.CharField(max_length=1000)
	def __unicode__(self):
		return self.choice_text	

class Quiz_Problem_Solutions(models.Model):
	problem=models.ForeignKey(Quiz_Problems)
	correct_choice=models.ForeignKey(Quiz_Problem_Choices)
	tutor_explanation=models.CharField(max_length=1000)
	def __unicode__(self):
		return self
