from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    return f'Hello {name}'

@app.route('/repeat/<word>/<int:num>')
def repeat(word, num):
    return f"{word * num}"
if __name__=="__main__":
    app.run(debug=True)