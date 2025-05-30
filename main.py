import os
from flask import Flask
from src.routes.dog_routes import dog_blueprint

app = Flask(__name__)
app.register_blueprint(dog_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
