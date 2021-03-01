from flask import Flask
from jinja2 import Template

app = Flask(__name__)

home_page = Template('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{{title}}</title>
    </head>
    <body>
        <h1>{{content}}</h1>
        {{link}}
    </body>
    </html>
    ''')

@app.route('/')
def home():
    title = 'home'
    content = 'home page'
    link = '''
        <a href="/about">ABOUTE</a> <br> <br>
        <a href="/product">PRODUCT</a> <br> <br>
        <a href="/help">HELP</a>
    '''

    return home_page.render(title=title, content=content, link=link)

    
@app.route('/about')
def about():
    title = 'about'
    content = 'about page'
    link = '''
        <a href="/">HOME</a>
    '''
    return home_page.render(title=title, content=content, link=link)


@app.route('/product')
def product():
    title = 'product'
    content = 'product page'
    link = '''
        <a href="/">HOME</a>
    '''
    return home_page.render(title=title, content=content, link=link)


@app.route('/help')
def help():
    title = 'help'
    content = 'help page'
    link = '''
        <a href="/">HOME</a>
    '''
    return home_page.render(title=title, content=content, link=link)

app.run(debug=True)