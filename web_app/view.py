from flask import render_template
from web_app import app

@app.route('/index')
def index():
    return render_template('/index.html')
