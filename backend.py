from flask import Flask, jsonify, request, render_template, session , redirect

from get_sql_connection import get_sql_connection
from get_all_products import get_all_products
from user import login 
from user import register
from get_del_product import del_product
from Add_product import order
from order import insert_order
from get_all_order import get_order_products 



app = Flask(
    __name__,
    template_folder="C:/Users/Sudeb Barman/Documents/Local Groccery/.vscode/Backend/UI/html",
    static_folder="C:/Users/Sudeb Barman/Documents/Local Groccery/.vscode/Backend/UI/html"
)

app.secret_key = "grocery_secret_key"


# LOGIN PAGE

@app.route("/login", methods=["GET", "POST"])
def login_page():

    if request.method == "POST":

        name = request.form["user_name"]
        password = request.form["password"]
        role = request.form["role"]

        connection = get_sql_connection()

        result = login(connection, name, password, role)

        if result:

            session["user_id"] = result[0]
            session["user_name"] = result[1]
            session["role"] = result[2]

            if role == "admin":
                return redirect("/dashboard")

            elif role == "subadmin":
                return redirect("/dashboard")

            elif role == "customer":
                return redirect("/customer")

        return render_template(
            "login.html",
            error="Invalid username, password or role"
        )

    return render_template("login.html")


# REGISTER PAGE

@app.route("/register", methods=["GET", "POST"])
def register_page():

    if request.method == "POST":

        name = request.form["user_name"]
        ph = request.form["ph_no"]
        password = request.form["password"]
        role = request.form["role"]

        connection = get_sql_connection()

        register(
            connection,
            name,
            ph,
            password,
            role
        )

        return redirect("/login")

    return render_template("register.html")


@app.route("/")
def first():
    return render_template("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/login")



# HOME PAGE

@app.route("/index")
def inde():

    if "user_id" not in session:
        return redirect("/login")

    if session["role"]=="customer":
        return redirect("/customer")

    
    return render_template("index.html")

@app.route("/api/orders", methods=["GET"])
def orders():

    connection = get_sql_connection()

    result = get_order_products(connection)

    return jsonify(result)


# DASHBOARD PAGE // GET ALL PRODUCTS PAGE

@app.route("/dashboard")
def home():
    if "user_id" not in session:
        return redirect("/login")

    if session["role"]=="customer":
        return redirect("/customer")
    
    return render_template("dashboard.html")


# GET ALL PRODUCTS

@app.route("/api/products", methods=["GET"])
def products():

    connection = get_sql_connection()

    result = get_all_products(connection)

    return jsonify(result)


# ADD PRODUCT PAGE

@app.route("/products")
def new_order_page():

    if "user_id" not in session:
        return redirect("/login")

    if session["role"]=="customer":
        return redirect("/customer")


    return render_template("products.html")

#ADD PRODUCT 

@app.route("/api/products", methods=["POST"])
def add_product():
    connection = get_sql_connection()
    DATA=request.json
    order(
        connection,
        DATA["product_name"],
        DATA["unit"],
        DATA["price"],

    )
    return jsonify({
        "massage":"product added successfully"
    })


# DELETE PRODUCT


@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    connection = get_sql_connection()

    del_product(
        connection,
        product_id
    )


    return jsonify({
        "message": "Product deleted successfully"
    })


#CUSTOMER PAGE

@app.route("/customer")
def customer_page():
    return render_template("customer_UI.html")

#SAVE ORDER 

@app.route('/api/orders', methods=['POST'])
def save_order():

    order = request.get_json()

    connection = get_sql_connection()

    order_id = insert_order(connection, order)

    return jsonify({
        "order_id": order_id,
        "message": "Order saved successfully"
    })


# START SERVER

if __name__ == "__main__":

    app.run(debug=True)

