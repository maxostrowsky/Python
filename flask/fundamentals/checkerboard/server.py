from flask import Flask, render_template
app = Flask(__name__)
    
@app.route('/')
def level_1():
    return render_template('index.html', num=8, num2=8, color1="red", color2="black")

@app.route('/<int:num>')
def level_2(num):
    return render_template('index.html', num=num, num2=8, color1="red", color2="black")

@app.route('/<int:num>/<int:num2>')
def level_3(num, num2):
    return render_template("index.html", num=num, num2=num2, color1="red", color2="black")

@app.route('/<int:num>/<int:num2>/<color1>/<color2>')
def colors(num, num2, color1="red", color2="black"):
    return render_template("index.html", num=num, num2=num2, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)