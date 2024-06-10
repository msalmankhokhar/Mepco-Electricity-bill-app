from flask import Flask, render_template, request, redirect
from requests import get
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    ref_no = request.args.get('ref_no')
    bill_response = get(f'https://bill.pitc.com.pk/mepcobill/general?refno={ref_no}').content
    soup = BeautifulSoup(bill_response, 'html.parser')
    base = soup.new_tag('base')
    base.attrs['href'] = 'https://bill.pitc.com.pk'
    soup.head.insert(0, base)
    return str(soup)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)