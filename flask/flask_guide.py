from flask import Flask
app = Flask(__name__)  # Making an web app instance of Flask and calling it "app".

@app.route("/")  # Location of function on webpage.
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)  # Runs the app. Debug mode gives additional information.
