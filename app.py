from flask import Flask, render_template, request

app = Flask(  # So that this is run instead of any other library code we write on initialization.
    __name__
)


@app.route("/")
def index():
    return render_template(  # Flask will use render_template to find the passed in html template, dynamic variable assignment in the brackets.
        "index.html"
    )


@app.route("/result")
def result():
    # name = request.args.get("name", "world")
    # return render_template("result.html")           # These two lines are the same thing as the single line return below.
    return render_template("result.html", name=request.args.get("name", "world"))
