from flask import Flask, render_template, request, g
from models.Cart import calculate_total

app = Flask(__name__)
app.config.from_pyfile("config.py")
app.config["SECRET_KEY"] = "test123"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/shoppingcart", methods=["POST"])
def shopping_cart():
    no_items = int(request.form.get("noItems", app.config.get("DEFAULT_NO_ITEMS")))
    price = float(request.form.get("price", app.config.get("DEFAULT_PRICE")))
    tax = float(request.form.get("tax", app.config.get("DEFAULT_TAX")))
    total = calculate_total(no_items, price, tax)

    return render_template(
        "shoppingcart.html",
        price=price,
        tax=tax,
        no_items=no_items,
        total=total,
    )