# Entry point of application

from app import create_app

app = create_app()

if __name__ == "__main__":
    # run on port 5005 (avoid conflicts)
    app.run(debug=True, port=5005)