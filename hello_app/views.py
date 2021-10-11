from flask import Flask, render_template
from datetime import datetime 
from . import app


@app.route("/") 
def home():
    return render_template("home.html")

@app.route("/about/")
def aboutus():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_name(name = None):
    return render_template(
        "hello_name.html",
        name=name,
        date=datetime.now().strftime("%A, %d %B, %Y at %X")
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

    


