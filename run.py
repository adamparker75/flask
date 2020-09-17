import os  # import os from the python library
from flask import Flask, render_template  # import the class Flask and the render_template

app = Flask(__name__)  # create an instance of the class and store in a variable called app the first argument os the name of the applications module


@app.route('/')  # when the root directory is browsed flask triggers this function
def index():
    return render_template("index.html")  # flask looks to templates directory to find the html


@app.route("/about")  # this is also called a view, which is looking at the about directory
def about():
    return render_template("about.html")  # whenever we navigate to /about, this template will be returned


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == '__main__':  # main is the name of the default module in python, it's the first one to run
    app.run(host=os.environ.get('IP'),  # these are the arguments we run our app with
            port=int(os.environ.get('PORT')),
            debug=True)  # dont use this in a production application
