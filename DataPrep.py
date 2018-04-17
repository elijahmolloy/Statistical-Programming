"""
Elijah Molloy
70 - 510 Spring I - 2018
18 FEB 2018

PROGRAMMING ASSIGNMENT #5
"""

from __future__ import division
import pandas as pd
import numpy as np


class DataPrep:
	def __init__(self):
		self.input_file = "energy.csv"

		self.countries_continents = None
		self.df = None

		self.run()


	@staticmethod
	def print_header_information():
		"""
		Heading Information
		:return:
		"""
		print "Elijah Molloy"
		print "70-510 - Spring 1 - 2018"
		print "Programming Assignment #5\n"


	@staticmethod
	def load_countries_continents():
		"""
		Returns the continent mapping file as a dictionary.
		:return:
		"""

		temp = {
			'Australia': 'Australia',
			'Austria': 'Europe',
			'Belgium': 'Europe',
			'Canada': 'North America',
			'Chile': 'South America',
			'CzechRepublic': 'Europe',
			'Denmark': 'Europe',
			'Estonia': 'Europe',
			'Finland': 'Europe',
			'France': 'Europe',
			'Germany': 'Europe',
			'Greece': 'Europe',
			'Hungary': 'Europe',
			'Iceland': 'Europe',
			'Ireland': 'Europe',
			'Israel': 'Asia',
			'Italy': 'Europe',
			'Japan': 'Asia',
			'Korea': 'Asia',
			'Luxembourg': 'Europe',
			'Mexico': 'North America',
			'Netherlands': 'Europe',
			'NewZealand': 'Oceania',
			'Norway': 'Europe',
			'Poland': 'Europe',
			'Portugal': 'Europe',
			'SlovakRepublic': 'Europe',
			'Slovenia': 'Europe',
			'Spain': 'Europe',
			'Sweden': 'Europe',
			'Switzerland': 'Europe',
			'Turkey': 'Asia',
			'UnitedKingdom': 'Europe',
			'UnitedStates': 'North America',
			'Brazil': 'South America',
			'China': 'Asia',
			'India': 'Asia',
			'Indonesia': 'Asia',
			'RussianFederation': 'Europe',
			'SouthAfrica': 'Africa'
		}

		return temp


	def read_input_file(self):
		"""
		This method will load energy.csv from the current directory
		into a pd.DataFrame. If the file cannot be found, the program
		will exit. Cells with a value of '..' will be replaced with np.nan
		for later manipulation.
		:return:
		"""

		try:
			# Read the csv, use col 0 as index, and replace '..' with NaN
			return pd.read_csv(self.input_file, index_col = 0).replace(to_replace = '..',
			                                            value = np.nan)

		# If there are any errors
		except AssertionError:
			print "Assertion Error: Exiting Program."
			quit()

		except TypeError:
			print "Type Error: Exiting Program."
			quit()

		except ValueError:
			print "Value Error: Exiting Program."
			quit()


	@staticmethod
	def cleanup_df(df):
		"""
		This method will replace the DataFrame's NaN values with the row average and will
		drop specified rows from the df.
		:param df: DataFrame
		:return: new DataFrame
		"""

		# Get all row's means excluding the NaN's
		means = df.mean(axis = 1)

		for i, column in enumerate(df):
			df.iloc[:, i] = df.iloc[:, i].fillna(means)

		# Drop the 3 specified rows from the df
		df = df.drop(labels = ['World', 'OECDtotal', 'EU27total'])

		return df



	@staticmethod
	def add_continents(df, countries_continents):
		"""
		Adds the continents to the df
		:param df:
		:param countries_continents:
		:return:
		"""

		# Add new column named Continent with the dictionary data
		df['Continent'] = pd.Series(countries_continents)

		return df


	def stat_analysis(self, df):
		"""
		Perform the specific statistical analysis specified for the assignment
		:param df:
		:return:
		"""
		indexes = df.Continent.unique()
		labels = ['num_countries', 'mean', 'small', 'avg', 'large']

		global_mean = df.mean().mean()
		global_std = df.std().std()

		data = []

		for index in indexes:
			# Get subset df
			temp_df = df[df['Continent'] == index]

			temp_std = temp_df.std().std()

			# Get values
			temp_num_countries = len(temp_df.index)
			temp_mean = temp_df.mean().mean()
			temp_small = 0
			temp_avg = 0
			temp_large = 0

			if global_mean - temp_std > temp_mean:
				temp_small = 1

			elif global_mean + temp_std < temp_mean:
				temp_large = 1

			else:
				temp_avg = 1

			data.append([
				temp_num_countries,
				temp_mean,
				temp_small,
				temp_avg,
				temp_large
			])

		final_df = pd.DataFrame(data = data, columns = labels, index = indexes)

		print final_df


	def run(self):
		"""
		This method ties together all of the methods above
		:return:
		"""
		self.print_header_information()

		self.countries_continents = self.load_countries_continents()

		self.df = self.read_input_file()
		self.df = self.cleanup_df(self.df)
		self.df = self.add_continents(self.df, self.countries_continents)

		self.stat_analysis(self.df)


if __name__ == "__main__":
	DataPrep()