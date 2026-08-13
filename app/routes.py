from flask import Blueprint, render_template, request
from app.database import get_db_connection

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Display the Northstar Support homepage."""
    return render_template("index.html")


@main.route("/order-status", methods=["GET", "POST"])
def order_status():
    """Allow customers to check their order status."""

    order = None
    error = None

    if request.method == "POST":
        order_number = request.form.get("order_number", "").strip().upper()

        if not order_number:
            error = "Please enter your order number."
        else:
            connection = get_db_connection()

            try:
                order = connection.execute(
                    """
                    SELECT
                        order_number,
                        customer_name,
                        product,
                        status,
                        expected_delivery
                    FROM orders
                    WHERE order_number = ?
                    """,
                    (order_number,)
                ).fetchone()

                if order is None:
                    error = (
                        "Order not found. "
                        "Please check your order number and try again."
                    )

            finally:
                connection.close()

    return render_template(
        "order_status.html",
        order=order,
        error=error
    )


@main.route("/returns", methods=["GET", "POST"])
def returns():
    """Allow customers to check return and refund information."""

    return_info = None
    error = None

    if request.method == "POST":
        order_number = request.form.get("order_number", "").strip().upper()

        if not order_number:
            error = "Please enter your order number."
        else:
            connection = get_db_connection()

            try:
                return_info = connection.execute(
                    """
                    SELECT
                        order_number,
                        product,
                        return_status,
                        instructions
                    FROM returns
                    WHERE order_number = ?
                    """,
                    (order_number,)
                ).fetchone()

                if return_info is None:
                    error = (
                        "No return information was found for this order. "
                        "Please check your order number and try again."
                    )

            finally:
                connection.close()

    return render_template(
        "returns.html",
        return_info=return_info,
        error=error
    )
