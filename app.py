from flask import Flask, request, render_template, redirect, flash, jsonify

from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "chickenzarecoolk21837"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

MOVIES = {"Add Movies"}


@app.route("/")
def home_page():
    """Shows home page"""
    return render_template("home.html")


@app.route("/old-home-page")
def redirect_to_home():
    """Redirects to new home page"""
    return redirect("/")


@app.route("/movies")
def show_all_movies():
    """Show list of all movies in fake DB"""
    return render_template("movies.html", movies=MOVIES)


@app.route("/movies/json")
def get_movies_json():
    return jsonify(list(MOVIES))


@app.route("/movies/new", methods=["POST"])
def add_movie():
    title = request.form["title"]
    # Add to pretend DB
    if title in MOVIES:
        flash("Movie Already Exists!", "error")
    else:
        MOVIES.add(title)
        flash("Created Your Movie!", "success")
    return redirect("/movies")


@app.route("/form")
def show_form():
    return render_template("form.html")


@app.route("/form-2")
def show_form_2():
    return render_template("form_2.html")


COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]


@app.route("/greet")
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliments=nice_thing)


@app.route("/greet-2")
def get_greeting_2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template(
        "greet_2.html",
        username=username,
        wants_compliments=wants,
        compliments=nice_things,
    )


@app.route("/lucky")
def lucky_number():
    num = randint(1, 10)
    return render_template("lucky.html", lucky_num=num, msg="You are so lucky!")
