from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config.from_pyfile(  # flask's version of the servlet context param name+value stuff
    "config.py"
)
app.config["SECRET_KEY"] = "test123"


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/shoppingcart", methods=["POST", "GET"])
def shopping_cart():
    price = float(
        request.form.get(
            "price", app.config["DEFAULT_PRICE"]
        )  # price is either provided in param "&price=x" or uses our default in our "context" config.py
    )
    no_items = int(request.form.get("no_items", app.config["DEFAULT_NO_ITEMS"]))
    tax = int(request.form.get("tax", app.config["DEFAULT_TAX"]))
    # tax = session.get("tax", app.config["DEFAULT_TAX"])

    total = no_items * price * (1 + tax / 100)
    return render_template(
        "shoppingcart.html", price=price, tax=tax, no_items=no_items, total=total
    )
