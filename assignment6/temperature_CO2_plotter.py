import pandas as pd
import matplotlib.pyplot as plt

def plot_co2(time_range=(1751, 2012), y_lim=None):
    """ Function for plotting CO2 over time. Takes optional arguments:
        time_range = (start_year, end_year)
        y_lim = (graph_y_min, graph_y_max) """

    co2_data = pd.read_csv("co2.csv", sep=",")

    # Cropping data to specified time-interval.
    co2_data = co2_data[co2_data["Year"] >= time_range[0]]
    co2_data = co2_data[co2_data["Year"] <= time_range[1]]

    if y_lim is None:    # Setting y_lim if not specified.
        y_lim = (0, 1.2*co2_data["Carbon"].max())

    co2_data.plot(x="Year", y="Carbon", kind="line", ylim=y_lim)
    print("hello")
    plt.savefig("fig/plot.png")

def plot_temperature(month, time_range=(1751, 2012), y_lim=None):
    """ Function for plotting temperature over time. Takes arguments:
        month = (month_to_plot)
        time_range = (start_year, end_year)
        y_lim = (graph_y_min, graph_y_max) """

    temp_data = pd.read_csv("temperature.csv", sep=",")

    # Cropping data to specified time-interval.
    temp_data = temp_data[temp_data["Year"] >= time_range[0]]
    temp_data = temp_data[temp_data["Year"] <= time_range[1]]

    # Setting y_lim if not specified.
    if y_lim is None:
        print(1.2*temp_data[month].max())
        y_lim = (temp_data[month].min()-1, temp_data[month].max()+1)
    temp_data.plot(x="Year", y=month, kind="line", ylim=y_lim)
    plt.show()
