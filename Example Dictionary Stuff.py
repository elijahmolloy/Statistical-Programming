"""
This file should show you how to check for values and add values to dictionaries
"""

# Create a new empty Dictionary
new_dictionary = {}
print new_dictionary


# To add values to a dictionary
new_dictionary["Example Key"] = "Example Value"
print new_dictionary


# To re-set value of Example Key in the dictionary. This will erase the
# previous value of 'Example Key' and set it to 'New Example Value'
new_dictionary["Example Key"] = "New Example Value"
print new_dictionary


# Check if the dictionary contains a specific key, there are two different main ways
print new_dictionary.get("Example Key")
# or
print new_dictionary["Example Key"]

# Using the dictionary.get(KEY) is better because it will return 'None' if the key doesnt exist
print new_dictionary.get("NON EXISTENT KEY")

# if you attempt to get a value from a key that does not exist using the second way, you will get an
# error if the key does not exist. So for attempting to get a value, the dictionary.get(KEY) is better.

# Un-comment out this line to show the error. Just as an example.
#print new_dictionary['NON EXISTENT KEY']


"""
So here, I'll try and go over an example of how to determine what cluster/centroid the point should go into.
I'll try and use code from the file I sent so you can work through it a little bit
"""

# These are the values from the input file the professor gave us.
input_file_list = [1.8, 4.5, 1.1,
                   2.1, 9.8, 7.6,
                   11.32, 3.2, 0.5, 6.5]

# In the example he gave us, he set k == 5, so we can use that as well.
k = 5

# The centroid is the point on the x-axis a particular cluster is located
centroids = dict(zip(range(k), input_file_list[0: k]))
print "\ncentroids = {}".format(centroids)

# The cluster is the collection of points from the input_file_list that are closest to that cluster's centroid
clusters = dict(zip(range(k), [[] for i in range(k)]))
print "\nclusters = {}".format(clusters)

"""
This part was a little confusing for me at first. Centroids and clusters are basically the same 
object, but refer to different information about the object

The centroid refers to the actual point in space (in our example, just an x-axis). The centroid
is the a actual point on the x-axis that a particular cluster is located

The cluster is the collection or group of points from the input_file_list that are closest to that 
cluster's centroid

SO basically, the centroid is the location in space (on the x-axis) that a particular cluster is located. The 
cluster itself just contains the points from the input_file_list that are closest to that cluster's centroid

For example, this is an x axis. There are three points on the x-axis, and 2 clusters.
The points will be represented by an <X>, and the Centroids will be represented by a <C>

		C1                      C2
		X                       X                        X
<------------------------------------------------------------------------------------------->
	0       2       4       6       8       10      12      14      16      18        20


In the example the professor gave us, he assigned the centroids of the clusters to the same 
points on the x-axis as the first k points from the input file
	( i.e. If the first 5 points from the input file at [1.8, 4.5, 1.1, 2.1, 9.8] and k == 5,
	  then the centroid of cluster one will be at 1.8
	  and the centroid of cluster two will be at 4.5
	  and the centroid of cluster three will be at 1.1
	  and the centroid of cluster four will be at 2.1
	  and the centroid of cluster five will be at 9.8 )
	  
In this example, there is a point at [1, 7, and 13]. We will assign the 2 clusters to have their centroids at
2 and 10. This is just to give them an initial value.

Now, we have to determine which point goes to which cluster. We do this by taking the 
absolute value of (the centroid point - the data point)

i.e. d(p, q) = |p - q|

This is just the distance on the x axis between the two points.

For each data point in [1, 7, 13], we want to check the distance between all potential clusters.

For data point 1,
	distance to cluster 1 == abs(1 - 1) == 0 (WINNER)
	distance to cluster 2 == abs(1 - 7) == 6 (LOSER)
	
	For data point 1, we want to assign the point to cluster one because it is the closest (distance of zero)
	
For data point 2,
	distance to cluster 1 == abs(1 - 7) == 6 (LOSER)
	distance to cluster 2 == abs(7 - 7) == 0 (WINNER)
	
	For this data point, we want to assign to cluster 2 because its closest.
	
For data point 3,
	distance to cluster 1 == abs(13 - 1) == 12 (LOSER)
	distance to cluster 2 == abs(13 - 7) == 6 (WINNER)
	
	For this data point, we want to assign to cluster 2 because it is also closest.
	
This is how the professor wanted us to store the data
"""

# The centroid is the point on the x-axis a particular cluster is located
centroids = dict(zip(range(k), input_file_list[0: k]))
print "\ncentroids = {}".format(centroids)


# The cluster is the collection of points from the input_file_list that are closest to that cluster's centroid
clusters = dict(zip(range(k), [[] for i in range(k)]))
print "\nclusters = {}".format(clusters)


# Create an empty dictionary for the data_points
data_points = {}

# And assign a key value for each of the data points in the input_file_list
# All this does is assign a point in the dictionary for each of the data_points
# in the input file list. We can assign the actual centroid point later.
for point in input_file_list:
	data_points[point] = None

"""
So right now, we have four different variables

input_file_data: this is a list of data points 'extracted' from the input file the professor gave us
	it contains floats (numbers with a decimal place) for all of the data_points located on the x-axis
	
centroid: this is a dictionary of the center points of the clusters. The initial values of the centroids are
	located at the first k points of the data_points in the input_file_list.
	
cluster: this is a dictionary of the data_points from the input_file_list that are closest to that cluster's
	centroid. 
	
data_points: this is a dictionary that contains all of the data_points in the input_file_list. It will keep track of 
	which cluster the data_point belongs to.
"""


"""
This method will go through the data points and and determine which point they are closest to
After determining which centroid it is closest to, it will add that data point to the cluster with
the closest centroid.

After adding the point to the cluster, it will update the centroid in the data_points.
"""

# For each of the points from the input_file_list
for point in input_file_list:
	# We set the min_distance == max(input_file_list) because the first iteration through the loop will re-set it
	# to the centroid that is closer.
	# The min_centroid is the actual centroid or cluster that the data point is currently closest to.

	min_distance = max(input_file_list)
	min_centroid = 0

	# For each of the centroids
	for centroid in centroids:

		# This is the abs(p - q) from earlier
		temp_distance = abs(centroids[centroid] - point)

		# if the distance to the current centroid is closer than the previous ones,
		# reset the values of the min distance to the new, lower distance
		# and set the value of the min centroid to that centroid
		if temp_distance < min_distance:
			min_distance = temp_distance
			min_centroid = centroid

	# After looping through the second for loop, the min_distance and min_centroid
	# variables contain the centroid which is closest to that specific data_point
	# Now we want to update the clusters value list with the data point

	# Because the values of the clusters dictionary is a list, we can add the current point to that list
	clusters[min_centroid].append(point)

	# Now we also want to update the centroid location to the data point in the data_points dictionary
	data_points[point] = min_centroid



print "\n#####################"
print "\nclusters : {}".format(clusters)
print "\ncentroids : {}".format(centroids)
print "\ndata_points : {}".format(data_points)

"""
So now, the next step is to update the values of of the centroids by taking all the data_points 
that belong to one specific cluster, suming them and taking the average, then updating the centroid point as the new
average.

For example:
	Cluster 0 = [1.8]
	Cluster 1 = [4.5, 6.5] This one will have to be updated. the current centroid of cluster 1 is 4.5
		To update this one, we take (4.5 + 6.5) / 2 == 11.0 / 2 == 5.5
		5.5 will be the new value
	Cluster 2 = [1.1, 0.5] This one will have t be updated too. 
		(1.1 + 0.5) / 2 == 1.7 / 2 = .85
		0.85 will be the new value
	
	Same proceedure for cluster 3 and 4.
"""


# This just takes the average of the data points at a specific cluster, and updates the centroid based upon
# the average of the data_points in that cluster.
for cluster in clusters:
	centroids[cluster] = sum(clusters[cluster]) / len(clusters[cluster])

print "\ncentroids : {}".format(centroids)

"""
The next step is to repeat the steps to
	1. Go through each data-point and determine which cluster it is closest to.
		a. Assign that data point to the cluster by updating the data_points dictionary and updating the clusters dictionary.
	2. Update the location of the centroids by finding th average of the data points in that cluster.

Those two steps will be continued until there are no more updates to the centroids of the clusters. At that point,
the data is stabilized and the algorithm is complete. We can exit the loop at this point. 
"""