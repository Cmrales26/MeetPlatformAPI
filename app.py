from flask import Flask
from routes.user_routes import user_routes
from routes.business_routes import business_routes
from routes.event_routes import event_routes
from routes.event_routes_user import User_events_routes
from dotenv import load_dotenv
import os


load_dotenv(".env")

app = Flask(__name__)

app.register_blueprint(user_routes, url_prefix="/api")
app.register_blueprint(business_routes, url_prefix="/api")
app.register_blueprint(event_routes, url_prefix="/api")
app.register_blueprint(User_events_routes, url_prefix="/api")


port = os.getenv("PORT")

if __name__ == "__main__":
    port = os.getenv("PORT", "456")
    app.run(debug=True, port=port)
