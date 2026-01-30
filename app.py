import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Cloud Run + Jenkins!"

def start_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Only start server if RUN_SERVER=true
    if os.environ.get("RUN_SERVER", "false").lower() == "true":
        start_server()
