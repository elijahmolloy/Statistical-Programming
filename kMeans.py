"""
Elijah Molloy
Felicia Cobb
70 - 510 Spring I - 2018
20 JAN 2018

PROGRAMMING ASSIGNMENT #2
"""

from __future__ import division


class kMeans:
	"""
	This class will accept user input for an input file with 1-dimensional
	data points, and output file, and a specific number of clusters. The
	class will then perform a k-means algorithm on the input data and will
	print results to the specified output file.

	It is important for the user to correctly place the input file in the
	same directory as this .py file. This program will only find the input file
	if the file is found in the same directory as this file.

	The output filename must also be unique and a .txt file and will be created
	in the same directory as this .py file
		(i.e. "this_is_my_output_file.txt")
	"""
	def __init__(self):
		self.input_filename = ""
		self.output_filename = ""
		self.k = 0
		self.input_file_data = []

		self.centroids = None
		self.clusters = None
		self.point_assignment = None
		self.previous_point_assignment = None

		self.run()


	@staticmethod
	def print_header_information():
		"""
		Heading Information
		:return:
		"""
		print "Elijah Molloy / Felicia Cobb"
		print "70-510 - Spring 1 - 2018"
		print "Programming Assignment #2\n"


	@property
	def get_input_filename(self):
		"""
		returns self.input_filename
		:return:
		"""
		return self.input_filename


	@property
	def get_output_filename(self):
		"""
		returns self.output_filename
		:return:
		"""
		return self.output_filename


	def set_input_filename(self):
		"""
		Sets or updates the name of self.input_filename.
		:return:
		"""
		self.input_filename = raw_input("\nEnter the name of the input file: ")


	def set_output_filename(self):
		"""
		Sets or updates the name of self.output_filename.
		:return:
		"""
		self.output_filename = raw_input("\nEnter the name of the output file: ")


	def set_number_of_clusters(self):
		"""
		Attempt to get self.number_of_clusters as a positive int input from user.
		Continue loop inside of method until user input is valid.
		:return:
		"""
		try:
			temp_number_of_clusters = int(raw_input("\nEnter the number of clusters: "))

			# If input was greater than 0
			if temp_number_of_clusters > 0:
				self.k = temp_number_of_clusters

			else:
				print "Input has to be an int value greater than 0. " \
				      "Please enter a positive int for the number of clusters."

				# Attempt to get new user input
				self.set_number_of_clusters()

		# If input is not an int, display error and attempt to get new user input
		except ValueError:
			print "Previous input is not an int. " \
			      "Please enter a positive int for the number of clusters."

			self.set_number_of_clusters()


	def open_and_read_input_file(self):
		"""
		Attempt to open self.input_filename. If error, get new self.input_filename and try again.
		If no error, populate self.input_file_data using list comp.
		:return:
		"""
		try:
			file_stream = open(self.get_input_filename, "r")

			# Get data from file_stream using list comp
			self.input_file_data = [float(line.rstrip()) for line in file_stream]

		# If self.input_filename cannot be found/opened
		except IOError:
			print "ERROR: {} could not be opened.".format(self.get_input_filename)

			# Attempt to get new input file name and read data
			self.set_input_filename()
			self.open_and_read_input_file()


	def initialize_variables(self):
		"""
		Initialize self.centroids, self.clusters, and self.point_assignment
		Assigns random values of centroid clusters
		:return:
		"""
		self.centroids = dict(zip(range(self.k), self.input_file_data[0 : self.k]))
		self.clusters = dict(zip(range(self.k), [ [] for i in range(self.k)]))


	@staticmethod
	def assign_to_clusters(data, centroids, clusters):
		"""

		:param data: self.input_file_data
		:param centroids: self.centroids
		:param clusters: self.clusters
		:return: updated_centroids, updated_clusters
		"""
		temp_point_assignment = {}

		# For each data point in self.input_file_data
		for data_point in data:
			min_distance = max(data)
			min_centroid = 0

			# For each centroid
			for centroid in centroids:
				temp_distance = abs(centroids[centroid] - data_point)

				# If the distance from the data_point to the centroid is closer than previous, reassign centroid
				if temp_distance < min_distance:
					min_distance = temp_distance
					min_centroid = centroid

			# Update the minimum centroid distance with the data_point
			clusters[min_centroid].append(data_point)

			temp_point_assignment[data_point] = min_centroid

		return centroids, clusters, temp_point_assignment


	@staticmethod
	def update_centroids(clusters, centroids):
		"""

		:param clusters:
		:param centroids:
		:return:
		"""
		for cluster in clusters:
			centroids[cluster] = sum(clusters[cluster]) / len(clusters[cluster])

		return centroids


	@staticmethod
	def point_assignments_are_stabilized(previous_point_assignment, point_assignment):
		"""
		Checks if the previous point assignment and current point assignments are equal or not
		:param previous_point_assignment:
		:param point_assignment:
		:return:
		"""
		if not previous_point_assignment or not point_assignment:
			return False

		if point_assignment == previous_point_assignment:
			return True

		return False


	def write_point_assignments_to_file(self):
		"""
		Writes the file based on the output name specified by the user.
		:return:
		"""
		f = open(self.output_filename, "w+")

		for point in self.point_assignment:
			f.write("Point {} is in cluster {}\n".format(point, self.point_assignment[point]))

		f.close()


	@staticmethod
	def print_clusters(clusters):
		"""
		Method used to print cluster point as specified in the assignment instructions
		:param clusters:
		:return:
		"""
		for point in clusters:
			print "{} : {}".format(point, clusters[point])


	def run(self):
		"""
		Engine of the class. This method will ensure correct functioning of the program
		and will orchestrate the class methods above.
		:return:
		"""

		self.print_header_information()

		# Get input from from the user
		self.set_input_filename()
		self.set_output_filename()
		self.set_number_of_clusters()

		# Attempt to prepare data for k-means algorithm
		self.open_and_read_input_file()
		self.initialize_variables()

		# Algorithm ready to be run
		data_stabilized = False
		iteration = 1

		# While the centroids are not stabilized
		while not data_stabilized:
			print "\nIteration {}".format(iteration)

			# Store previous point assignment if the dictionary is not empty
			if not self.point_assignment:
				self.previous_point_assignment = {}

			else:
				self.previous_point_assignment = self.point_assignment

			# Assign data points to centroids
			self.centroids, self.clusters, self.point_assignment = self.assign_to_clusters(
				self.input_file_data, self.centroids, self.clusters)

			# Update the centroid locations
			self.centroids = self.update_centroids(self.clusters, self.centroids)

			# Print new clusters
			self.print_clusters(self.clusters)

			# If data is stabilized, exit loop
			if self.point_assignments_are_stabilized(self.previous_point_assignment, self.point_assignment):
				data_stabilized = True

			# Else data is not stabilized
			else:
				# Re-initialize self.clusters
				self.clusters = dict(zip(range(self.k), [[] for i in range(self.k)]))
				iteration += 1

		# Write data to output file
		self.write_point_assignments_to_file()


if __name__ == "__main__":
	kMeans()



