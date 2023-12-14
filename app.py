from flask import Flask, render_template, request, redirect, url_for

import config
from gpt import gpt_response

app = Flask(__name__)
app.logger.setLevel(config.LOG_LEVEL)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':

        if len(request.form) > 3:

            res, _ = gpt_response(config.GPT_CONFIG, request.form.get('ingredients'))

            return render_template("result.html", result=res)

        return redirect(url_for('result'))

    return redirect(url_for('result'))


if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.DEBUG)
