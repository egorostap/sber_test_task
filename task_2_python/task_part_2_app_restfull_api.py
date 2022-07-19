from flask import Flask, render_template, request
from flask_restful import Api, Resource
import requests
from local import *

app = Flask(__name__)

# ссылка для проверки: http://127.0.0.1:5000/endpoint/tags
@app.route('/endpoint/tags', methods=['POST', 'GET'])
def take_tags():
    if request.method == 'POST':
        url = request.form['url']
        answer = count_tags(url)
        return answer
    return render_template('tags.html')


if __name__ == "__main__":
    app.run(debug=True)
