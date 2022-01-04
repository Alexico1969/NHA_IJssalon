
from os import getenv, environ
from flask import Flask, render_template, session, request, redirect, url_for, g


app=Flask(__name__, static_url_path='/static')

app.secret_key = 'Bruce Wayne is Batman'

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/prijzen', methods=['GET', 'POST'])
def prijzen():
   return "prijzen"

@app.route('/recepten', methods=['GET', 'POST'])
def recepten():
   return "recepten"



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

