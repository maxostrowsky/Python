from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_ninjas, model_dojos
from flask_app.models.model_dojos import Dojo

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    model_ninjas.Ninja.create(request.form)
    id = request.form['dojo_id']
    return redirect(f'/dojo/{id}')

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template('add_ninja.html', all_dojos = dojos)

# @app.route('/ninja/<int:id>/edit')
# def edit_ninja():
#     pass

# @app.route('/ninja/<int:id>/update', methods=['POST'])
# def update_ninja():
#     pass

# @app.route('/ninja/<int:id>/delete', methods=['GET'])
# def delete_ninja():
#     pass