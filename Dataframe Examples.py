from __future__ import division
import pandas as pd

"""
This file explores some of topics studied for the Week 4 HW.

Adding data to dataframes, manipulating the data, and what-not.

Before creating a dataframe, we first have to prepare the data. For the example
that the professor shows us, we can create a list for easy manipulation and 
data checking
"""

example_data = [
			['ford','mustang','coupe','A'], # 1st entry
			['chevy','camaro','coupe','B'], # 2nd entry
			['ford','fiesta','sedan','C'], # 3rd entry
			['ford','focus','sedan','A'], # 4th entry
			['ford','taurus','sedan','B'], # 5th entry
			['toyota','camry','sedan','B'] # 6th entry
		]



"""
example_data is just a list of strings. This is what is known as a 2-dimensional array/list.
The call it two dimensional because each index of example_data contains another array.

We can return individual arrays by using the following
"""
print "\n1st entry = {}".format(example_data[0]) # will print the 1st entry in example_data
print "\n2nd entry = {}".format(example_data[1]) # will print the 2nd entry in example_data



"""
To get specific values from the arrays, we can specify their location in both arrays at the same time
"""
print "\n1st entry from 1st array = {}".format(example_data[0][0])



"""
Before adding the example_data to a df, we also need the names of the columns.

For this we will create another 1-dimensional list of the names of the columsn in the order they appear
"""
cols = ['make', 'model', 'type', 'rating']
print "\ncols = {}".format(cols)



"""
So now that we have our example_data prepared, we can add it to a dataframe using the following command 
"""
example_df = pd.DataFrame(example_data, columns=cols)

print "\nexample_df = {}".format(example_df)



"""
A df is basically an excel file. It keeps tracks of different entries where each entry can have different 
columns of whatever type of data youre keeping track of.

For the example_df, we are keeping track of different cars, and each of the cars make, model, type, and rating.

We also want to perform different statistical analysis of the cars. The first is the type probability of a car
occuring with a specific type of rating. 

I know you said in your text that you had already figures this out, but I'll go over it any way. The 
probability of a specific rating occuring would be the 

== (number of cars with a specific ratings) / (total number of cars)

So, in order to find the percentage of cars with each particular rating, we first have to figure out 
how many ratings there are. What if the professor enters only cars with ratings 'A'?
Or what if he enters ratings as 'A' and 'C' only? First thing we have to do is determine what 
categories of ratings there are. To do this, we run the following command
"""
ratings = example_df.rating.unique()
print "\nratings = {}".format(ratings)


"""
That command will search through the df for unique entries in the 'rating' column.

Please note that if we had specified  

	cols = ['MAKE', 'MODEL', 'TYPE', 'RATING']

Then we would have to type 

	ratings = example_df.RATINGS.unique()
	
	
Next, we need to determine the total number of rows in the dataframe. This will tell us how many 
cars are in the df. There are a few different ways to do this, but I think the easiest is using this
command.
"""
size_of_df = len(example_df.index)
print "\nsize of example_df = {}".format(size_of_df)



"""
Now what we can do is iterate through the list of ratings, and determine the probability of a specific rating
occuring for the entire sample of car data.

First, we have to get the number of occurances of a specific rating occuring throughout the entire df.
Then, after finding out how many cars have that specific rating, divide by the total number of cars in the df.

That will give us a probability of a specific rating occurring for that specific rating.

We can iterate through the list of ratings using a FOR loop, and can find the number of occurances using
df.value_counts[rating]
"""

for rating in ratings:
	print "\nAttempting to find the rating for == {}".format(rating)

	rating_count = example_df.rating.value_counts()[rating]
	print "Number of occurances of {} == {}".format(rating, rating_count)

	probability = rating_count / size_of_df
	print "Probability of {} == {}".format(rating, probability)

	print "Probability trimed to 6 decimal points == {}".format(format(probability, '.6f'))



"""
So that one way to find probabilities of one specific rating for the entire df,
but what about conditional probabilities?

To find the conditional probabilities, we first have to find sub-sets of the df depending
on the second parameter of the conditional probability statement.

So, for example, if we are supposed to find 

	prob (type = 'sedan' | rating = 'A') 

What we are asked to do is find the probability of a car being a sedan IF the rating == A.

So what we have to do is get a sub-set of the entries from the df where the rating == A, then
see out of all those entries, how many have the type == sedan, coupe, etc.

The first thing to do is find all of the types of cars in the df. We can do something 
similar to what we did for ratings, except for the type.
"""
types = example_df.type.unique()
print "\ntypes = {}".format(types)



"""
Now what we have to do is iterate through all of the ratings, and for each rating,
find the conditional probability of each type of car occuring.

This part is a little confusing because we have to use try/catch blocks.

A try/catch block is a way to handle errors in code. 

For example, lets say you go to a store and try to buy something, but when you swipe your debit
card, you accidentally enter the wrong pin. You arent allowed to spend the money on that try because
the pin is incorrect and the screen says "You entered the wrong pin" or something like that.

a try/catch block in programming is similar to that. Its when you try to do something in code
that you arent supposed to do. Except, with a try/catch block, you can tell the computer what to do when an error
is encountered, like when the grocery store thing says "You entered the wrong pin!"

What we are going to attempt to do is iterate through all of the ratings, and for each rating, check
the conditional probability of each different type of car. But what if the sub-df doesnt contain a specific 
type of car? For example, what if for rating == C, there is only type == sedan in the sub_df?

Using the specific command we are going to use, if we search for a specific
value in the df that is not there, the code will throw an error. The error means that the 
value we are searching for does not exist in the df. When that happens, we have to use a try/catch block to
say 'hey code. no problem. because you couldnt find the value means that there are 0 occurances of that 
type of car for that specific rating.'
"""

for rating in ratings:
	print "\n##########################################"
	print "\nAttempting to find sub-df where rating == {}".format(rating)

	sub_df = example_df[example_df['rating'] == rating]
	print "\nsub_df = {}".format(sub_df)

	type_count = 0

	for type in types:
		print "\n     Attempting to find number of occurances type == {}".format(type)

		try:
			type_count = sub_df.type.value_counts()[type]
			print "     type_counts == {}".format(type_count)

		except KeyError:
			print "     Uh oh! sub_df does not contain an entry where type == {}".format(type)
			print "     Setting the number of occurances to 0."

		sub_df_len = len(sub_df.index)
		probability = format(type_count / sub_df_len, '.6f')

		print "\nProb({} | {}) == {}".format(type, rating, probability)

