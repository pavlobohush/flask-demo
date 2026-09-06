import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello():
    hemmelighet = os.getenv("SECRET_MESSAGE", "ingen hemmelighet satt")
    return f"<h1>Hei fra Flask!</h1><p>{hemmelighet}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
