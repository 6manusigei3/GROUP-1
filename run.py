
from app import create_app
from app.database import initialize_database

app = create_app()

initialize_database()


if __name__ == "__main__":
    app.run(debug=True)
