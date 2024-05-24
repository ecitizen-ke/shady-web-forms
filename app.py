from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)

posts = [
    {"title": "Post 1", "description": "Python is great"},
    {"title": "Post 2", "description": "C# is the best"},
]

app.config["SECRET_KEY"] = "21e3367163225c129615869b0a84ffd2dc64177564df2062"


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/create")
def create():
    return render_template("create.html")


@app.route("/store", methods=["POST"])
def store():
    title = request.form["title"]
    description = request.form["description"]
    if not title:
        flash("Title is required")
    elif not description:
        flash("Description is required")
    else:
        posts.append({"title": title, "description": description})
        return redirect(url_for("index"))
