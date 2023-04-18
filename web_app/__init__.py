from flask import Flask, request, send_from_directory, jsonify, render_template, send_file
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

# configfileの読み込み
app.config.from_object('web_app.config')


# iconの設定
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico', )


from web_app import view
