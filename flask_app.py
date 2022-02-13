
from os import getenv, environ
from flask import Flask, render_template, session, request, redirect, url_for, g
from helper import prijs

app=Flask(__name__, static_url_path='/static')

app.secret_key = 'Bruce Wayne is Batman'

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/prijzen', methods=['GET', 'POST'])
def prijzen():
    items = [
        {
            "product": "vanille-ijs 1 liter",
            "prijs" : prijs(3)
        }, 
    {
            "product": "chocolade-ijs 1 liter",
            "prijs" : prijs(3)
        }
    ]
    return render_template("prijzen.html", items=items)

@app.route('/recepten', methods=['GET', 'POST'])
def recepten():
    items = [
        {
            "recept": "Tiramisu di nona",
            "img" : "tiramisu.png"
        }, 
    {
            "recept": "IJstaart met chocolade",
            "img" : "ijstaart.png"
        }
    ]
    return render_template("recepten.html", items=items)



# Do not alter this if statement below
# This should stay towards the bottom of this file
if __name__ == "__main__":
    flask_env = getenv('FLASK_ENV')
    if flask_env != 'production':
        environ['FLASK_ENV'] = 'development'
        app.debug = True
        app.asset_debug = True
        server = Server(app.wsgi_app)
        server.serve()
    app.run()

