from flask import Flask, render_template
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

    return render_template('index.html', title=title, content=content)

    
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