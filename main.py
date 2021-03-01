from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'home'
    content = 'home page'
    link = 'Home'

    return render_template('index.html', title=title, content=content, link=link)

    
@app.route('/about')
def about():
    title = 'about'
    content = 'about page'
    link = 'home'
    
    return render_template('index.html', title=title, content=content, link=link)


@app.route('/product')
def product():
    title = 'product'
    content = 'product page'
    link = 'home'

    return render_template('index.html', title=title, content=content, link=link)


@app.route('/help')
def help():
    title = 'help'
    content = 'help page'
    link = 'home'

    return render_template('index.html', title=title, content=content, link=link)

app.run(debug=True)