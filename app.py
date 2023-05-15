from flask import Flask
from route.route import route
import os

debug = os.environ.get("DEBUG")
print(debug)

app = Flask(__name__, static_url_path='/', static_folder='./static')
app.register_blueprint(route)

if __name__ == '__main__':
    app.run(debug=debug, host='0.0.0.0')