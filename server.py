from flask import Flask
from flask import jsonify
from models.Users import Users

app = Flask(__name__)

@app.route("/users")
def get_all_users():
    usersHandler = Users()
    u = usersHandler.all()
    return jsonify(u)


@app.route("/users/<id>")
def get_user(id):
    usersHandler = Users()
    u = usersHandler.find(id)
    return jsonify(u)