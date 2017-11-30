import os
from flask import Flask, render_template
from temperature_CO2_plotter import plot_co2, plot_temperature

current_dir = os.path.dirname(__file__)
if not os.path.exists( os.path.join(current_dir, "fig") ):
    os.mkdir("fig")

app = Flask(__name__, static_folder=current_dir)

@app.route("/")
def frontpage():
    return render_template("frontpage.html")

@app.route("/co2/<years_input>")
def get_co2(years_input):
    time_range = (float(years_input[:4]), float(years_input[4:]))
    print(time_range)
    plot_co2(time_range)
    return render_template("plotpage.html")

if __name__ == "__main__":
    app.run(debug=True)
