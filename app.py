from flask import Flask, render_template, request, flash
import json
import config
from gpt import gpt_response


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.logger.setLevel(config.LOG_LEVEL)
app.secret_key = config.FLASK_SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        res, _ = gpt_response(gpt_config=config.GPT_CONFIG, ingredients=ingredients, debug=config.GPT_DEBUG)

        res = json.loads(res)

        if 'dishes' in res:
            return render_template("home.html", result=res.get('dishes'))
        else:
            flash(message=res['error'],  category='error')

    return render_template('home.html')


if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.DEBUG)
