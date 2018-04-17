"""
Elijah Molloy
Felicia Cobb
Robinson Mikowlski
70 - 510 Spring I - 2018
30 JAN 2018

PROGRAMMING ASSIGNMENT #3
"""

from __future__ import division
import numpy as np


class NearestNeighbor:
	"""
	This class will perform general a general NN algorithm on sample training and testing data.
	It will iterate through the testing data by comparing it to the training data, calculating
	the classification of the testing data based upon the closest neighboring data point.
	"""
	def __init__(self):
		self.__TRAINING_FILE_NAME = "iris-training-data.csv"
		self.__TESTING_FILE_NAME = "iris-testing-data.csv"

		self.training_values = None
		self.training_labels = None
		self.testing_values = None
		self.testing_labels = None

		self.run()


	@staticmethod
	def print_header_information():
		"""
		This method will print the heading information of the members of group 18,
		the title of this course, along with semester and year, and the title of week three's
		programming assignment.
		:return:
		"""
		print "Elijah Molloy\nFelicia Cobb\nRobinson Mikowlski"
		print "70-510 - Spring 1 - 2018"
		print "Programming Assignment #3\n"


	@staticmethod
	def read_file_for_values_and_labels(file_name):
		"""
		This method will open a file_stream from file_name as read-only using iteration.
		The line will be split into a 1-D array with 5 variables
			i.e. [5.0, 3.0, 1.6, 0.2, 'Iris-setosa']
		The first 4 variables of each line will be stored into a 2-D values array named values
			i.e. values.append([5.0, 3.0, 1.6, 0.2])
		The last variable of each line will be stored into a 1-D labels array.
			i.e. labels.append('Iris-setosa')
		:param file_name: the name of the file attempting to be opened
		:return: values, labels
		"""
		# Initializing a 2-D array to hold float values
		values = []

		# Initialize a 1-D array to hold labels
		labels = []

		# Attempt to open file_stream and pull information from file
		try:
			file_stream = open(file_name, "r")

			# For each line in the file
			for line in file_stream:
				# Turn the line into a 1-D array[float, float, float, float, string]
				temp = line.rstrip().split(",")

				# Add float values to 2-D values array
				values.append(temp[0:4])

				# Add string label to 1-D labels array
				labels.append(temp[4])

			# Return 2-D values array and 1-D labels array
			return np.array(values), np.array(labels)

		# If the file cannot be opened or read, kill the program
		except IOError:
			print "{} could not be opened. Exiting program"
			quit() # Kill the program


	@staticmethod
	def calculate_distance(training_array, testing_array):
		"""
		This method will create temporary variables for each of the variables in each of the
		arrays, and will calculate the distance between two different points in 4-D space using the
		formula in the programming assignment description.
		:param training_array: a 1-D array with 4 elements
				i.e. [3.5, 4.2, 9.2, 7.5]
		:param testing_array: a 1-D array with 4 elements
				i.e. [3.5, 4.2, 9.2, 7.5]
		:return: the distance between the two points
		"""
		# Turn input arrays into temp variables for easier math visualization
		sl_1, sw_1, pl_1, pw_1 = [float(i) for i in training_array]
		sl_2, sw_2, pl_2, pw_2 = [float(i) for i in testing_array]

		# 4-D distance formula
		return np.sqrt(((sl_1 - sl_2) ** 2) + ((sw_1 - sw_2) ** 2) + ((pl_1 - pl_2) ** 2) + ((pw_1 - pw_2) ** 2))


	def run(self):
		"""
		This method will orchestrate the logic provided in the methods above. it will satisfy the requirements
		provided in Week 3's programming assignment instructions provided on BlackBoard.

		1. This method will populate self.training_values and self.training_labels using
			self.read_file_for_values_and_labels(self.__TRAINING_FILE_NAME)
		2. This method will populate self.testing_values and self.testing_labels using
			self.read_file_for_values_and_labels(self.__TESTING_FILE_NAME)
		3. This method will calculate the distance from each testing data point to all training data points
			in an effort to guess which flower classification the testing data is.

			For each data point in self.testing_values
				- Create a temp 1-D array, determine the distance from that testing point to each
					of the training points using self.calculate_distance, and add that distance to the
					temp 1-D array.
				- Select the training label of the closest point in that array by getting the index
					of the minimum value in that array. That minimum index will allign with the same index
					of the self.training_labels.
				- Print predicted and actual label.
				- Update the correct guesses and total guesses number.
		4. Print accuracy.
		:return:
		"""
		self.print_header_information()

		# Get training file data
		self.training_values, self.training_labels = self.read_file_for_values_and_labels(
			self.__TRAINING_FILE_NAME)

		# Get testing file data
		self.testing_values, self.testing_labels = self.read_file_for_values_and_labels(
			self.__TESTING_FILE_NAME)

		# Variables to record accuracy
		total_guesses = 0
		correct_guesses = 0

		print "#\tTrue\t\tPredicted"

		# For each value in self.testing_values
		for i in range(self.testing_values.__len__()):

			# temp 1-D array to record distances from values in self.training_values
			distances = []

			# For each value in self.training_values
			for j in range(self.training_values.__len__()):
				# Add the distance between the testing_value to the training_value
				distances.append(self.calculate_distance(self.testing_values[i], self.training_values[j]))

			"""
			The index of the minimum distance in the distances array is that testing value's nearest neighbor.
			It means that index is the location in the training_labels and training_values of the current testing_value 
			closest point.
			We can retrieve the guess label from self.training_labels[nearest_neighbor_index]
			We can find the correct label from self.testing_labels[i]
					(i == array index for the current testing_value)
			"""

			nearest_neighbor_index = distances.index(min(distances))
			guess_label = self.training_labels[nearest_neighbor_index]
			correct_label = self.testing_labels[i]

			# Print i + 1, correct label, and guess label
			print "{}\t{}\t{}".format(i + 1, correct_label, guess_label)

			# increment total number of guesses
			total_guesses += 1

			# If the guess label is the same as the correct label, increment correct guesses count
			if guess_label == correct_label:
				correct_guesses += 1

		print "\nAccuracy: {}%".format((correct_guesses / total_guesses) * 100)


if __name__ == "__main__":
	NearestNeighbor()