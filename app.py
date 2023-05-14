from flask import Flask
from route.API import api
from route.route import route

app = Flask(__name__, static_folder="static")
app.register_blueprint(api)
app.register_blueprint(route)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')