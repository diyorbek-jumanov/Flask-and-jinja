from flask import Flask

app = Flask(__name__)

home_page = '''
    <a href="/about">ABOUTE</a> <br> <br>
    <a href="/product">PRODUCT</a> <br> <br>
    <a href="/help">HELP</a>
'''

@app.route('/')
def home():
    return home_page

    
@app.route('/about')
def about():
    return '<a href="/">HOME</a>'


@app.route('/product')
def product():
    return '<a href="/">HOME</a>'

@app.route('/help')
def help():
    return '<a href="/">HOME</a>'

app.run(debug=True)