"""
I'll try to walk through Nearest Neighbor algorithm for better understanding with the code

The first part of the algorithm is to upload the data from the files that the Professor gave us.
"""

from __future__ import division
import numpy as np

"""
The first step to running the algorithm is to retreive the data from
the files that the professor gave us.
"""


# Just a variable that holds the name of the file the professor gave us
__TRAINING_FILE_NAME = "iris-training-data.csv"


# These lists will hold the data found in the file from above
# While we are initializing the variables as regular lists, when we actually
# add data to them, they will turn into numpy.ndarrays
TRAINING_VALUES = []
TRAINING_LABELS = []


# To get info from the file, we have to open it first.
# The "r" just means that we want to read from the file. If we used "w"
# we could also write information to the file as well.
file_stream = open(__TRAINING_FILE_NAME, "r")


"""
Now that we have a file_stream to the file open, we can go through the entire file line
by line and get the data that we need.

It is important to understand how we are storing the data found in the file
Each line in the file represents the data from a specific flower. i.e.

File line 1 == Flower 1
File line 2 == Flower 2
File line 3 == Flower 3
and so on...

When we retrieve the data from the file, we are doing so one line at a time. So we will get
the flower one information first, do some manipulation to it, and store it. after we get and store
that line's data, we will move onto the next line and will repeat for each line of data in the file.
"""


# For each line of data in the file_stream
for line in file_stream:

	# Store the data from the line as a temporary list. Split the data in the line
	temp = line.rstrip().split(",")
	print temp

	# Add the first 4 values of that line's data to the TRAINING_VALUES list
	# These 4 values corespond to only the numerical data from that line
	TRAINING_VALUES.append(temp[0:4])
	print temp[0:4]

	# The last value represents the label of that flower.
	# We will add the label to the TRAINING_LABEL list
	TRAINING_LABELS.append(temp[4])
	print temp[4]


"""
That is basically it for getting the data from the training file.

It is important to note that we have stored the values into the arrays in the same order we 
read them from the file.

i.e. training_labels = [Line_1 Label,
							Line_2 Label,
							Line_3 Label,
							Line_4 Label,
							Line_5 Label,
							and so on...
							]
							
i.e. training_values = [
							[line 1 a, line 1 b, line 1 c, line 1 d],
							[line 2 a, line 2 b, line 2 c, line 2 d],
							[line 3 a, line 3 b, line 3 c, line 3 d],
							[line 4 a, line 4 b, line 4 c, line 4 d],
							[line 5 a, line 5 b, line 5 c, line 5 d],
							and so on...
						]
							
So we can get the line one label by finding the first item in the list. We can find the line two label
by finding the second item in the list and so on.
"""

# Here we just transform the regular arrays to np.ndarrays
TRAINING_VALUES = np.array(TRAINING_VALUES)
TRAINING_LABELS = np.array(TRAINING_LABELS)
