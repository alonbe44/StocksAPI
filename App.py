from authlib.oauth2.rfc6750 import BearerToken
from flask import jsonify, request
import main
from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from functools import wraps
from flask import Flask, request, jsonify
from authlib.integrations.flask_oauth2 import AuthorizationServer, ResourceProtector, current_token
from authlib.oauth2.rfc6749 import grants
from werkzeug.security import gen_salt
from authlib.oauth2.rfc6749 import ClientAuthentication
from authlib.oauth2.rfc6749.errors import InvalidClientError

from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth


from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'test'



# Configuration
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)

# Dummy user data (replace with DB in real app)
USERS = {
    "admin": "admin"
}

# Route to login and get a token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    # Simple auth check
    if USERS.get(username) != password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Protected route
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200





# for connectivity test only
@app.route('/',methods=['GET'])
def index():
    return jsonify("Stocks API Connection Pass"),200
@app.route('/allStocks',methods=['GET'])
def AllStocks():
    return jsonify(main.get_sp500_tickers()),200

@app.route('/Stocks/<string:StockName>',methods=['GET'])
def Get_Stock(StockName):
    return jsonify(main.get_single_Stock_Data(StockName)),200

@app.route('/Stocks/<string:StockName>/history',methods=['GET'])
@jwt_required()
def Get_Stock_History(StockName):
    return (main.get_stock_history(StockName)),200

@app.route('/FaangStocks',methods=['GET'])
def Get_Faang_Stock():
    return (main.get_stock_data(main.faang_plus)),200


if __name__ == '__main__':
    app.run(debug=True,port=5000)