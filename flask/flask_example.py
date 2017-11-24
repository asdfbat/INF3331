from flask import Flask, render_template
app = Flask(__name__)  # Making an web app instance of Flask and calling it "app".

@app.route("/")  # Location of function on webpage.
def hello():
    return "Hello, World!"

@app.route("/<username>")    # Route can take arguments, using <>
def show_username(username):    # which must also be arguments to the function
    return "User = %s" % username    # and can then be accessed inside the function.

@app.route("/post/")
@app.route("/post/<name>")    # This will match both /post/ and /post/<name>.
def post(name=None):    # We must therefore give <name> a default value, in case not provided.
    return render_template("flask_template.html", name=name)    # Takes our HTML-template and
                                                                # inserts our name varaible.
if __name__ == "__main__":
    app.run(debug=True)  # Runs the app. Debug mode gives additional information on errors.
