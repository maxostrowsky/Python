from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_dojos, model_ninjas
from flask_app.models.model_dojos import Dojo


@app.route('/')
@app.route('/dojo')
def index():
    context = {
    'all_dojos' : model_dojos.Dojo.get_all()
    }
    return render_template('index.html', **context)

@app.route('/dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    id = model_dojos.Dojo.create(request.form)
    return redirect('/dojo')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    context = {
        'dojos' :model_dojos.Dojo.get_dojo_with_ninjas({"id":id})
    }
    return render_template('show_dojo.html', **context)

@app.route('/dojo/<int:id>/edit')
def edit_dojo():
    pass

@app.route('/dojo/<int:id>/update', methods=['POST'])
def update_dojo():
    pass

@app.route('/user/<int:id>/delete', methods=['GET'])
def delete_user():
    pass