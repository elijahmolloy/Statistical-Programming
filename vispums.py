"""
Elijah Molloy
Felicia Cobb
Robinson Mikowlski
70 - 510 Spring I - 2018
21 February 2018

PROGRAMMING ASSIGNMENT #6
"""

from __future__ import division
from scipy import stats
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Vispums:
	def __init__(self):
		self.file_name = 'ss13hil.csv'
		self.df = None

		self.run()


	@staticmethod
	def read_file_for_data(file_name):
		"""
		This method will accept a file_name, read the file as a .csv, and return a pd.DataFrame
		representation of the information found in the file

		:param file_name: name of file
		:return: pd.DataFrame
		"""

		try:
			return pd.read_csv(file_name).replace(to_replace = '..', value = np.nan)

		except IOError:
			print "Error reading {}. Exiting program.".format(file_name)
			quit()


	@staticmethod
	def prepare_pie_chart(df, ax):
		"""
		This method will accept a pd.DataFrame and a location to a previously established
		subplot position. It will perform necessary logic on the DataFrame, construct a Pie Chart
		from the data, and will add it to the ax position. It will construct a pie chart containing
		the number of household records for different values of the HHL (household language)
		attribute. The plot should have no wedge labels, but should have a legend in the
		upper left corner.

		:param df: pd.DataFrame
		:param ax: sub-plot position
		:return:
		"""

		# Data Storage variables
		pie_data = [0, 0, 0, 0, 0]
		pie_data_labels = ['English Only', 'Spanish', 'Other Indo-European', 'Asian and Pacific Island Languages', 'Other']
		pie_chart_color = ['blue', 'green', 'red', 'lightblue', 'purple']
		pie_chart_wedgeprops = {'linewidth' : 1, 'edgecolor' : "black"}

		# Total Number of Entries
		pie_data_total = len(df.HHL.dropna().index)

		# Calculate Percentage of Language and add to Data Storage variable
		for i in range(1, 6):
			pie_data[i - 1] = (df.HHL.value_counts()[i] / pie_data_total) * 100

		# Construct Pie Chart at Sub-Position
		patches, text = ax.pie(pie_data, startangle = 242, colors = pie_chart_color, wedgeprops = pie_chart_wedgeprops)
		ax.set_title('Household Languages', fontsize = 10)
		ax.legend(patches, pie_data_labels, loc = "upper left", prop = {'size' : 8})
		ax.axis('equal')


	@staticmethod
	def prepare_histogram(df, ax):
		"""
		This method will accept a pd.DataFrame and a location to a previously established
		subplot position. It will perform necessary logic on the DataFrame, construct a Histogram
		from the data, and will add it to the ax position. It will construct a histogram of HINCP
		(household income) with KDE plot superimposed. You should use a log scale
		on the x-axis with log-spaced bins.

		:param df: pd.DataFrame
		:param ax: sub-plot position
		:return:
		"""

		# Gather relevant data
		hist_data = df.HINCP.dropna().tolist()

		# Prepare KDE Data
		kde = stats.gaussian_kde(hist_data)
		kde_linespace = np.logspace(1, 6)

		# Construct Histogram at Sub-Position
		ax.hist(hist_data, density = True, bins = np.logspace(1, 6), alpha = 0.7,
		        edgecolor = 'black', linewidth = '0.5', color = 'green')
		ax.set_title('Distribution of Household Income', fontsize = 10)
		ax.set_xlabel('Household Income ($) - Log Scaled', fontsize = 8)
		ax.set_ylabel('Density', fontsize = 8)
		ax.set_xscale('log')
		ax.set_xlim(10)
		ax.tick_params(axis = 'both', labelsize = 8)

		# Construct KDE line at Sub-Position
		ax.plot(kde_linespace, kde(kde_linespace), color = 'black', linestyle = '--', linewidth = 1)


	@staticmethod
	def prepare_bar_chart(df, ax):
		"""
		This method will accept a pd.DataFrame and a location to a previously established
		subplot position. It will perform necessary logic on the DataFrame, construct a Bar Chart
		from the data, and will add it to the ax position. It will construct a bar chart of Thousands of
		Households for each VEH (vehicles available) value (exclude NaN). Make sure to use
		the WGTP value to count how many households are represented by each household record
		and divide the sum by 1000.

		:param df: pd.DataFrame
		:param ax: subplot position
		:return:
		"""

		# Data Storage variables
		bar_chart_data = [0, 0, 0, 0, 0, 0, 0]
		bar_chart_labels = ['0', '1', '2', '3', '4', '5', '6']

		# Calculate Totals based on WGTP value
		for i in range(0, 7):
			temp_df = df[df['VEH'] == i]
			bar_chart_data[i] = temp_df['WGTP'].dropna().sum() / 1000

		# Construct Bar Chart at Sub-Position
		ax.bar(bar_chart_labels, bar_chart_data, align = 'center', color = 'red',
		       edgecolor = 'black', linewidth = '0.5')
		ax.set_title('Vehicles Available in Households', fontsize = 10)
		ax.set_xlabel('# of Vehicles', fontsize = 8)
		ax.set_ylabel('Thousands of Households', fontsize = 8)
		ax.tick_params(axis = 'both', labelsize = 8)
		ax.set_ylim(0, 1800)


	@staticmethod
	def prepare_scatter_plot(df, ax, fig):
		"""
		This method will accept a pd.DataFrame and a location to a previously established
		subplot position. It will perform necessary logic on the DataFrame, construct a Scatter Plot
		from the data, and will add it to the ax position. It will construct a scatter plot of TAXP
		(property taxes) vs. VALP (property value). Make sure to convert TAXP into the
		appropriate numeric value, using the lower bound of the interval. Use WGTP as the
		size of each marker, <o> as the marker type, and MRGP (first mortgage payment) as
		the color value. Add a colorbar.

		:param df: pd.DataFrame
		:param ax: sub-plot position
		:param fig: figure
		:return:
		"""

		# Get sub dataframes
		temp_df = df[['VALP', 'TAXP', 'WGTP', 'MRGP']].dropna()
		temp_df = temp_df[temp_df.TAXP != 1]

		taxp_dict = {
			2  : 1,
			3  : 50,
			4  : 100,
			5  : 150,
			6  : 200,
			7  : 250,
			8  : 300,
			9  : 350,
			10 : 400,
			11 : 450,
			12 : 500,
			13 : 550,
			14 : 600,
			15 : 650,
			16 : 700,
			17 : 750,
			18 : 800,
			19 : 850,
			20 : 900,
			21 : 950,
			22 : 1000,
			23 : 1100,
			24 : 1200,
			25 : 1300,
			26 : 1400,
			27 : 1500,
			28 : 1600,
			29 : 1700,
			30 : 1800,
			31 : 1900,
			32 : 2000,
			33 : 2100,
			34 : 2200,
			35 : 2300,
			36 : 2400,
			37 : 2500,
			38 : 2600,
			39 : 2700,
			40 : 2800,
			41 : 2900,
			42 : 3000,
			43 : 3100,
			44 : 3200,
			45 : 3300,
			46 : 3400,
			47 : 3500,
			48 : 3600,
			49 : 3700,
			50 : 3800,
			51 : 3900,
			52 : 4000,
			53 : 4100,
			54 : 4200,
			55 : 4300,
			56 : 4400,
			57 : 4500,
			58 : 4600,
			59 : 4700,
			60 : 4800,
			61 : 4900,
			62 : 5000,
			63 : 5500,
			64 : 6000,
			65 : 7000,
			66 : 8000,
			67 : 9000,
			68 : 10000
		}

		valp_list = temp_df.VALP.tolist()
		taxp_list = map(taxp_dict.get, temp_df.TAXP.tolist())
		wgtp_list = [ x / 8 for x in temp_df.WGTP.tolist()]
		mrgp_list = temp_df.MRGP.tolist()

		scatter_cmap = plt.cm.get_cmap('coolwarm')

		# Construct Scatter Plot at Sub-Position
		im = ax.scatter(valp_list, taxp_list, s = wgtp_list, c = mrgp_list, vmin = 0, vmax = 5000, cmap = scatter_cmap, alpha = .3)
		ax.set_title('Property Taxes vs. Property Values', fontsize = 10)
		ax.set_xlabel('Property Value ($)', fontsize = 8)
		ax.set_ylabel('Taxes ($)', fontsize = 8)
		ax.set_xlim(0, 1200000)
		ax.tick_params(axis = 'both', labelsize = 8)

		# Add color bar here....
		scatter_cbar = fig.colorbar(im, ax = ax)
		scatter_cbar.ax.set_ylabel('First Mortgage Payment (Monthly $)', fontsize = 8)
		scatter_cbar.ax.tick_params(axis = 'both', labelsize = 8)


	def run(self):
		"""
		Main method. Builds the graphs, adds sub-graphs by calling methods above and adding
		them to their appropriate section. Saves the graph as a .png
		:return:
		"""
		self.df = self.read_file_for_data(self.file_name)

		# Declare Graph
		fig, ax = plt.subplots(nrows = 2 , ncols = 2,
		                       sharex = 'none', sharey = 'none')
		fig.set_size_inches(11.5, 8, forward = True)

		# Generate Graphs as Subplots
		self.prepare_pie_chart(self.df, ax[0][0])
		self.prepare_histogram(self.df, ax[0][1])
		self.prepare_bar_chart(self.df, ax[1][0])
		self.prepare_scatter_plot(self.df, ax[1][1], fig)

		# Tight layout pls
		plt.tight_layout()

		# Save as .png
		plt.savefig('pums.png', orientation = 'landscape', papertype = 'letter')


if __name__ == "__main__":
	Vispums()