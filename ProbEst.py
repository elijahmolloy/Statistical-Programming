"""
Elijah Molloy
70 - 510 Spring I - 2018
11 FEB 2018

PROGRAMMING ASSIGNMENT #4
"""

from __future__ import division
import pandas as pd


class ProbEst:
	"""
	This class will accept input from the user in the form of details of automobiles
	and will perform some statistical analysis based upon the rating and the type
	of car.
	"""
	def __init__(self):
		self.number_of_instances = 0
		self.data_cols = ['make', 'model', 'type', 'rating']
		self.data = pd.DataFrame(columns = self.data_cols)

		self.run()


	@staticmethod
	def print_header_information():
		"""
		This method will print the heading information of the members of group 18,
		the title of this course, along with semester and year, and the title of week three's
		programming assignment.
		:return:
		"""
		print "Elijah Molloy"
		print "70-510 - Spring 1 - 2018"
		print "PROGRAMMING ASSIGNMENT #4\n"


	def get_number_of_instances_from_user(self):
		"""
		This method will set self.number_of_instances to the input specified by the user
		If the user doesnt enter a number or if the number is negative or not an int,
		and error will be thrown and the user will be asked to re-enter the number.
		:return:
		"""
		try:
			# The int interpretation of the user input
			temp = int(raw_input("Enter the number of car instances: "))

			# If input is > 0
			if temp > 0:
				self.number_of_instances = temp

			# If input is <= 0
			else:
				print "Number has to be an int greater than 0. Please enter a number greater than 0."

				self.get_number_of_instances_from_user()

		# If user doesnt enter an int
		except Exception:
			print "Number was invalid. Please enter a positive number."

			self.get_number_of_instances_from_user()


	def compile_dataframe(self, number_of_instances):
		"""
		Compiles and returns a dataframe with input for each of the specified number_of_instances
		:param number_of_instances:
		:return:
		"""
		# Variables for the data frame
		data = []

		# For each of the specified number of instances
		for number in range(number_of_instances):
			# Get data from the user
			self.data.loc[number] = self.get_car_input_from_user()


	def compile_dataframe_default(self):
		"""
		For help with debugging.
		:return:
		"""
		data = [
			['ford','mustang','coupe','A'],
			['chevy','camaro','coupe','B'],
			['ford','fiesta','sedan','C'],
			['ford','focus','sedan','A'],
			['ford','taurus','sedan','B'],
			['toyota','camry','sedan','B']
		]

		self.data = pd.DataFrame(data, columns = self.data_cols)


	def get_car_input_from_user(self):
		"""
		This method will continue to run until the user has successfuly entered
		4 terms split by a ','
		:return: input split into a list
		"""
		try:
			# Attempt to get user input, strip, and split into a list
			temp = raw_input("\nEnter the make,model,type,rating: ").replace(" ", "").split(",")

			# If there are 4 terms
			if temp.__len__() == 4:
				return temp

			# Else the user needs to re-enter input correctly
			else:
				print "Please ensure there are 4 terms per line"
				return self.get_car_input_from_user()

		# If there is any random error
		except Exception:
			print "Please ensure you split terms with a ',' and that there are only 4 terms"
			return self.get_car_input_from_user()


	def analysis_of_dataframe(self, dataframe):
		"""
		Performs some statistical analysis of the information found in the dataframe
		:param dataframe:
		:return:
		"""
		types = self.data.type.unique()
		ratings = self.data.rating.unique()

		print ""

		# First analysis section
		for rating in ratings:
			percentage = format(self.data.rating.value_counts()[rating] / len(self.data.index), '.6f')

			# Print probability data
			print "Prob(rating={}) = {}".format(rating, percentage)

		print ""

		# Second analysis section
		for rating in ratings:
			for type in types:

				# Get sub-set dataframe
				temp_dataframe = self.data[self.data['rating'] == rating]

				# Get conditional probability
				try:
					percentage = format(temp_dataframe.type.value_counts()[type] / len(temp_dataframe.index), '.6f')

				# Current type not found in temp_dataframe
				except KeyError:
					percentage = format(0, '.6f')

				# Print probability data
				finally:
					print "Prob(type={}|rating={}) = {}".format(type, rating, percentage)


	def run(self):
		"""
		This method ties all the methods above together.
		:return:
		"""
		self.print_header_information()

		#self.get_number_of_instances_from_user()

		#self.compile_dataframe(self.number_of_instances)

		print "\n{}".format(self.data)

		# Uncomment these lines for debugging
		self.compile_dataframe_default()
		# print "\n{}".format(self.data)

		self.analysis_of_dataframe(self.data)


if __name__ == "__main__":
	ProbEst()
