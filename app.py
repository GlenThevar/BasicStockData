from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
swagger = Swagger(app)

class StockInformation(Resource):
    def get(self):
        """
        This method responds to the GET request for retrieving stock information.
        ---
        tags:
        - Stock Information
        parameters:
            - name: ticker
              in: query
              type: string
              required: true
              description: The stock symbol (ticker) for which information is requested.
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            information:
                                type: object
                                description: Information about the specified stock
            400:
                description: Bad Request. Invalid or not found stock symbol.
            500:
                description: Internal Server Error. Issue with retrieving stock information.
        """
        ticker_symbol = request.args.get('ticker')
        if not ticker_symbol:
            return jsonify({"error": "Stock symbol (ticker) is required"}), 400
        try:
            stock = yf.Ticker(ticker_symbol)
            if stock is None:
                return jsonify({"error": f"Invalid or not found stock symbol: {ticker_symbol}"}), 400
            stock_info = stock.info
            return jsonify({"information": stock_info})
        except Exception as e:
            error_message = f"Internal Server Error. {str(e)}"
            return jsonify({"message": error_message}), 500
        
api.add_resource(StockInformation, "/stock-information")

if __name__ == "__main__":
    app.run(debug=True)
