from flask import Flask, render_template
import config

app = Flask(__name__)
app.logger.setLevel(config.LOG_LEVEL)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.DEBUG)
