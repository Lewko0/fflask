from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    with open('templates/index.html', 'r', encoding='utf-8') as stream:
        return stream.read()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)