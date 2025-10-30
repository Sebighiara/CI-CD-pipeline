from flask import Flask
import os

app = Flask(__name__)

#we use PORT from env var, default 8080
PORT = int(os.getenv("PORT", 8080))

@app.route("/")
def home():
	return "Hello, DevOps world!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=PORT)
