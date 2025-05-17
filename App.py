import main
from flask import Flask, redirect, url_for, session
from flask import request, jsonify
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required, get_jwt_identity)
from datetime import timedelta

app = Flask(__name__)



# Configuration
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)


# initialize Json Web Token to be related to this app
jwt = JWTManager(app)

#UserName and Password
USERS = {
    "admin": "admin"
}

# Route to login and return a token
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

# return top 500 Stocks
@app.route('/allStocks',methods=['GET'])
@jwt_required()
def AllStocks():
    return jsonify(main.get_sp500_tickers()),200

# return specific Stock Price for Current Date.
@app.route('/Stocks/<string:StockName>',methods=['GET'])
@jwt_required()
def Get_Stock(StockName):
    return jsonify(main.get_single_Stock_Data(StockName)),200

# return specific Stock Price for last 6 months
@app.route('/Stocks/<string:StockName>/history',methods=['GET'])
@jwt_required()
def Get_Stock_History(StockName):
    return (main.get_stock_history(StockName)),200

# return Fang Companies Stock Price for Today
@app.route('/FaangStocks',methods=['GET'])
@jwt_required()
def Get_Faang_Stock():
    return (main.get_stock_data(main.faang_plus)),200


@app.route('/marketStatus',methods=['GET'])
@jwt_required()
def Get_Market_Status():
    return main.get_market_status()


if __name__ == '__main__':
    app.run(debug=True,port=5000)