from flask import Flask, render_template, request
from models.models import URLShortner
from ..main import app


@app.route('/')
def index():
    return render_template('index.html', foo='bar')


@app.route('/save-url', methods=['POST'])
def encode():
    url = request.form['url']

    URLShortner.save_shorted_url(url)
    shorted_url = URLShortner.get_url(url)

    return render_template('result.html', shorted_url=shorted_url)
