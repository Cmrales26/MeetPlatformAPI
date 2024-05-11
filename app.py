from flask import Flask
from routes.user_routes import user_routes
import os

app = Flask(__name__)

app.register_blueprint(user_routes, url_prefix="/api")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "456"))
    app.run(debug=True, port=port)
