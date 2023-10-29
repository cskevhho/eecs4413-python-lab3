from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config.from_pyfile(  # flask's version of the servlet context param name+value stuff
    "config.py"
)
app.config["SECRET_KEY"] = "test123"


@app.route("/")
def index():
    price = float(request.args.get("price", app.config["DEFAULT_PRICE"])) # price is either provided in param "&price=x" or uses our default in our "context" config.py
    no_items = int(request.args.get("no_items", app.config["DEFAULT_NO_ITEMS"]))
    if "tax" in request.args:  # we check if we see 'tax' in the param line
        session["tax"] = float(request.args["tax"]) # if it is, we save that value to our "session", so testing curl commands, tax will stay at the provided param rate
    tax = session.get("tax", app.config["DEFAULT_TAX"])

    total = no_items * price * (1 + tax / 100)

    return render_template(
        "index.html", price=price, tax=tax, no_items=no_items, total=total
    )
