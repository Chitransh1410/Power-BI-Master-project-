from flask import Flask, jsonify
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route('/stocks')
def get_stocks():
    symbols = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'SBIN.NS', 'HDFCBANK.NS']
    rows = []
    for sym in symbols:
        stock = yf.Ticker(sym)
        info = stock.info
        rows.append({
            'Company': info.get('longName'),
            'Symbol': sym,
            'Current Price': info.get('currentPrice'),
            'Open': info.get('open'),
            'Day High': info.get('dayHigh'),
            'Day Low': info.get('dayLow'),
            'Previous Close': info.get('previousClose'),
            'Volume': info.get('volume'),
            'Market Cap': info.get('marketCap'),
            'P/E Ratio': info.get('trailingPE'),
            '52W High': info.get('fiftyTwoWeekHigh'),
            '52W Low': info.get('fiftyTwoWeekLow'),
            'Sector': info.get('sector'),
            'Industry': info.get('industry')
        })
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
