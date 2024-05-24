from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"title": "Post 1", "description": "Python is great"},
    {"title": "Post 2", "description": "C# is the best"},
]


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/create", methods=["GET", "POST"])
def create():
    return render_template("create.html")
