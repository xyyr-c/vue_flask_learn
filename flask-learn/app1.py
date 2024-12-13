from flask import Flask

app = Flask(__name__)

@app.route('//')
def index():
    return 'Hello, World!'
@app.route('/<name>/')
def name(name):
    return 'Hello, %s!' % name
@app.route('/ids/<int:id>/')
def ids(id):
    return 'ID: %d' % id
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)