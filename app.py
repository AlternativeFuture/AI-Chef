from flask import Flask, render_template, request, flash
import json
import json2table

import config
from gpt import gpt_response

app = Flask(__name__)
app.logger.setLevel(config.LOG_LEVEL)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        res, _ = gpt_response(gpt_config=config.GPT_CONFIG, ingredients=ingredients, debug=config.GPT_DEBUG)

        # import pdb;
        # pdb.set_trace()

        res = json.loads(res)

        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style": "width:100%"}
        html_element = json2table.convert(res,
                                          build_direction=build_direction,
                                          table_attributes=table_attributes)
        # import pdb; pdb.set_trace()

        if 'dishes' in res:
            return render_template("index.html", result=res.get('dishes'), html_element=html_element)
        else:
            flash(message=res['error'],  category='error')
            # return res['error']  # render_template("index.html", result=res.get('error'))

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.DEBUG)
