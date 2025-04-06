from flask import Flask, jsonify
import yfinance as yf
import os

app = Flask(__name__)

@app.route('/')
def get_stocks():
    symbols = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'SBIN.NS', 'HDFCBANK.NS']
    rows = []
    for sym in symbols:
        stock = yf.Ticker(sym)
        info = stock.info

        row = {
            'Company': info.get('longName') or sym,
            'Symbol': sym,
            'Current Price': info.get('currentPrice') or 0,
            'Open': info.get('open') or 0,
            'Day High': info.get('dayHigh') or 0,
            'Day Low': info.get('dayLow') or 0,
            'Previous Close': info.get('previousClose') or 0,
            'Volume': info.get('volume') or 0,
            'Market Cap': info.get('marketCap') or 0,
            'P/E Ratio': info.get('trailingPE') or 0,
            '52W High': info.get('fiftyTwoWeekHigh') or 0,
            '52W Low': info.get('fiftyTwoWeekLow') or 0,
            'Sector': info.get('sector') or 'N/A',
            'Industry': info.get('industry') or 'N/A'
        }
        rows.append(row)

    return jsonify(rows)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
