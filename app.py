from flask import Flask, render_template, request, redirect, url_for
import json

import config
from gpt import gpt_response

app = Flask(__name__)
app.logger.setLevel(config.LOG_LEVEL)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/recipe', methods=['POST'])
def recipe():
    if request.method == 'POST':

        ingredients = request.form.get('ingredients')

        if len(ingredients) > 3:

            res, _ = gpt_response(config.GPT_CONFIG, ingredients)
            # import pdb; pdb.set_trace()
            return render_template("index.html", result=json.loads(res).get('dishes'))

        return redirect(url_for('home'))

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.DEBUG)
