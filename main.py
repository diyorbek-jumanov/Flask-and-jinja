from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    title = 'index'
    content = 'home page'
    link = '''
        <a href="/about">ABOUTE</a> <br> <br>
        <a href="/product">PRODUCT</a> <br> <br>
        <a href="/help">HELP</a>
    '''
    home_page = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
    </head>
    <body>
        <h1>{content}</h1>
        {link}
    </body>
    </html>
    '''

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