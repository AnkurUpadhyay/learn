# import statements
from models import Course_Problemset
from models import Problemset_Problems
from models import Problemset_Problem_Choices
from models import Problemset_Problem_Solutions
from models import User
from models import Course_Details

class Course_Problemset_Fetch:
	def fetch_course_problemsets(self, course_id):
		course=Course_Details.objects.get(id=course_id)
		course_problemset_list=course.course_problemset_set.all()
		return course_problemset_list
		
	def fetch_problemset_problems(self, problemset_id):
		problemset=Course_Problemset.objects.get(id=problemset_id)
		problems_list=problemset.problemset_problems_set.all()
		problemset_problems_list={}
		for problem in problems_list:
			problem_choices=problem.problemset_problem_choices_set.all()
			problemset_problems_list[problem.problem_text]=problem_choices
		return problemset_problems_list
		
	def fetch_problemset(self, problemset_id):
		problemset=Course_Problemset.objects.get(id=problemset_id)
		return problemset
		
	def fetch_problem_solution(self, problem_id):
		problem=Problemset_Problems.objects.get(id=problem_id)
		problem_solution_list=problem.problemset_problem_solutions_set.all()
		return problem_solution_list
