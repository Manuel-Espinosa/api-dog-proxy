from flask import Flask
from flask_cors import CORS
from src.routes.dog_routes import dog_blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(dog_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
