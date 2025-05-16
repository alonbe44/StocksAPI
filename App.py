from flask import Flask, jsonify, request
import main

app = Flask(__name__)




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
def Get_Stock_History(StockName):
    return (main.get_stock_history(StockName)),200

@app.route('/FaangStocks',methods=['GET'])
def Get_Faang_Stock():
    return (main.get_stock_data(main.faang_plus)),200


if __name__ == '__main__':
    app.run(debug=True,port=8080)