import pandas as pd
import matplotlib.pyplot as plt

# Reads a csv file. "sep" decides what seperates data on each line.
bike_stats = pd.read_csv("trips-2017.10.1-2017.10.31.csv", sep=",")

print(type(bike_stats))  # "DataFrame" type object.
print(bike_stats)  # Prints nicely formated data.
print(bike_stats.head(10))  # The "head" method prints the first x rows of data
print(bike_stats.tail(5))  # The last rows.

# We can extract just the data in specific columns(all columns are named in csv files.)
start_stations = bike_stats["Start station"]
start_and_end_times = bike_stats[["Start time", "End time"]][5:10]  # Rows 5 through 10.

# Checking what data-type pandas interprets each column as:
print(bike_stats.dtypes)

# If something is interpreted wrong, we may specify it. For instance, Start and End time should be dates:
# bike_stats = pd.read_csv("trips-2017.10.1-2017.10.31.csv", sep=",", parse_dates=["Start time", "End time"])
# Note that pandas will convert the timezone to GMT

# The "DataFrame" type also has a plot method:
# bike_stats["Start station"].head().plot(kind="bar")
# bike_stats[["Start station", "End station"]].head().plot(kind="bar")
# bike_stats.head().plot(x="Start time", y=["Start station", "End station"], kind="bar")
# plt.show()

# Pandas can also save the data to a set of file formats, like Latex, Excel, HTML, numpy...
bike_stats.to_csv("data.csv")

# Counting the repeating occurrences of each value in a column:
# start_stations_count = bike_stats["Start station"].value_counts()[:10].plot(kind="bar")
# plt.show()

# We can also do mathematical operations on the columns
bike_stats["Start station"].min()
# And use condition in the indexing:
bike_stats[bike_stats["Start station"] > 30]  # Gives all columns with "Start station" > 30.

# We can also add new columns to the DataFrame instance:
bike_stats["Station difference"] = bike_stats["Start station"] - bike_stats["End station"]

# Extracting the data of a column into a numpy array:
numpy_array = bike_stats["Start station"].values

# Combining two DataFrames with the same column-types is done with the concat function
bike_stats2 = pd.concat((bike_stats_september, bike_stats_october))

# We can also merge two tables with the same number of rows (but different columns):
pd.merge(bike_stats, bike_stations_info)
