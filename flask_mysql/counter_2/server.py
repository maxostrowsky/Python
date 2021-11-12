from flask import Flask, session, render_template, redirect
app = Flask(__name__)
app.secret_key = "voldermort"

@app.route('/')
def count():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('count.html')

@app.route('/reset')
def reset():
    session.pop('count')
    return redirect('/')

@app.route('/add_count')
def add():
    session['count'] = session['count'] + 1
    return redirect('/')

if __name__=="main":
    app.run(debug=True)