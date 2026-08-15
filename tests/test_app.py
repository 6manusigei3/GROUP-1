
import unittest

from app import create_app


class NorthstarTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    # Test homepage
    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # Test Order Status page loads
    def test_order_status_page(self):
        response = self.client.get("/order-status")
        self.assertEqual(response.status_code, 200)

    # Test Returns page loads
    def test_returns_page(self):
        response = self.client.get("/returns")
        self.assertEqual(response.status_code, 200)

    # Test Order Status with no order number
    def test_order_status_empty_order_number(self):
        response = self.client.post(
            "/order-status",
            data={"order_number": ""}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Please enter your order number.",
            response.data
        )

    # Test Returns with no order number
    def test_returns_empty_order_number(self):
        response = self.client.post(
            "/returns",
            data={"order_number": ""}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Please enter your order number.",
            response.data
        )

    # Test a valid order number
    def test_valid_order_status(self):
        response = self.client.post(
            "/order-status",
            data={"order_number": "NS1001"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"NS1001", response.data)

    # Test an invalid order number
    def test_invalid_order_status(self):
        response = self.client.post(
            "/order-status",
            data={"order_number": "INVALID999"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Order not found.",
            response.data
        )

    # Test a valid return request
    def test_valid_return(self):
        response = self.client.post(
            "/returns",
            data={"order_number": "NS1001"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"NS1001", response.data)

    # Test an invalid return request
    def test_invalid_return(self):
        response = self.client.post(
            "/returns",
            data={"order_number": "INVALID999"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"No return information was found",
            response.data
        )


if __name__ == "__main__":
    unittest.main()
