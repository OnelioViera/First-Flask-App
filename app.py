from random import randint, choice, sample
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "chickenzarecoolk21837"
debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    html = """
    <html>
    <body>
    <h1>Home Page</h1>
    <p>Welcome to my simple app!</p>
    <a href='/'>Home Page</a>
    <br>
    <a href='/hello'>Go to the hello page</a>
    <br>
    <a href='/goodby'>Go to the goodby page</a>
    <br>
    <a href='/add-comment'>Add Comment</a>
    </body>
    </html>
    """
    return html


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


@app.route("/spell/<word>")
def spell_word(word):
    caps_word = word.upper()
    return render_template("spell_word.html", word=caps_word)


@app.route("/add-comment")
def add_comment_form():
    return """
   
    <h1>Add Comment</h1>
    <form method='POST'>
    <input type='text' placeholder='comment' name='comment'/>
    <br>
    <input type='text' placeholder='username' name='username'/>
    <br>
    <button>Submit</button>
    </form>
    <a href='/'>Home Page</a>
   
"""


@app.route("/add-comment", methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
    <h1>Saved Your Comment</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>        
    </ul>
    <a href='/'>Home Page</a>
"""


@app.route("/hello")
def say_hello():
    """Shows hello apge"""
    return render_template("hello.html")


@app.route("/goodbye")
def say_goodbye():
    html = """
    <html>
    <body>
    <h1>Goodbye!</h1>
    <p>This is the goodbye page</p>
    <a href='/'>Home Page</a>
    <br>
    <a href='/hello'>Go to the hello page</a>
    </body>
    </html>
    """
    return html


@app.route("/search")
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1> <p>Sorting By: {sort}</p>"


# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "You Made A Post Request!"

# @app.route("/post", methods=["GET"])
# def get_demo():
#     return "You Made A Get Request!"

# @app.route("/add-comment")
# def add_comment_form():
#     return """

#     <h1>Add Comment</h1>
#     <form method='POST'>
#     <input type='text' placehloder='comment' name='comment'/>
#     <button>Submit</button>
#     </form>

# """

# @app.route("/add-comment", methods=["POST"])
# def save_comment():
#     return """
#     <h1>Saved Your Comment!</h1>
# """
