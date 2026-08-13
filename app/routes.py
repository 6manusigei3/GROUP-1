from flask import Blueprint, render_template, request
from app.database import get_db_connection

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/order-status", methods=["GET", "POST"])
def order_status():
    order = None
    error = None

    if request.method == "POST":
        order_number = request.form.get("order_number", "").strip().upper()

        if not order_number:
            error = "Please enter an order number."
        else:
            connection = get_db_connection()

            order = connection.execute(
                """
                SELECT *
                FROM orders
                WHERE order_number = ?
                """,
                (order_number,)
            ).fetchone()

            connection.close()

            if order is None:
                error = "Order not found. Please check the order number."

    return render_template(
        "order_status.html",
        order=order,
        error=error
    )


@main.route("/returns", methods=["GET", "POST"])
def returns():
    return_info = None
    error = None

    if request.method == "POST":
        order_number = request.form.get("order_number", "").strip().upper()

        if not order_number:
            error = "Please enter an order number."
        else:
            connection = get_db_connection()

            return_info = connection.execute(
                """
                SELECT *
                FROM returns
                WHERE order_number = ?
                """,
                (order_number,)
            ).fetchone()

            connection.close()

            if return_info is None:
                error = "No return information was found for this order."

    return render_template(
        "returns.html",
        return_info=return_info,
        error=error
    )
