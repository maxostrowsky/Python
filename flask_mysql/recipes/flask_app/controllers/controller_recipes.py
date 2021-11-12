from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_recipes, model_users
from flask_bcrypt import Bcrypt



bcrypt = Bcrypt(app)



@app.route('/dashboard')
def success():
    if 'uuid' not in session:
        return redirect('/')
    user = model_users.User.get_one({'id':session['uuid']})
    recipe = model_recipes.Recipe.get_all()
    return render_template('dashboard.html', all_recipes=recipe, user = user)

@app.route('/recipe/new', methods=['POST'])
def add_recipe():
    if not model_recipes.Recipe.recipe_validation(request.form):
        return redirect('/new')
    else:
        data = {
            **request.form,
            'user_id':session['uuid']
        }
        model_recipes.Recipe.create(data)
        return redirect('/dashboard')


@app.route('/new')
def new_recipe():
    
    return render_template('add_recipe.html')

@app.route('/recipe/<int:id>')
def show_recipe(id):
    user = model_users.User.get_one({'id':session['uuid']})
    recipe = model_recipes.Recipe.get_one({"id":id})
    if not recipe:
        return redirect('/dashboard')
    return render_template('show_recipe.html', recipe=recipe, user=user)


@app.route('/edit/<int:id>')
def edit_recipe(id):
    recipe = model_recipes.Recipe.get_one({"id":id})
    if not recipe:
        return redirect('/dashboard')
    if recipe.user_id != session['uuid']:
        return redirect('/dashboard')
    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/edit/<int:id>/update', methods=['POST'])
def update_receipe(id):
    if not model_recipes.Recipe.recipe_validation(request.form):
        return redirect(f'/edit/{id}')
    data = {
        **request.form,
        'id': id
    }
    model_recipes.Recipe.update_one(data)
    return redirect(f'/recipe/{id}')

@app.route('/edit/<int:id>/delete', methods=['get'])
def delete_recipe(id):
    recipe = model_recipes.Recipe.get_one({'id':id})
    if not recipe:
        return redirect('/dashboard')
    if recipe.user_id != session['uuid']:
        return redirect('/dashboard')
    model_recipes.Recipe.delete_one({'id':id})
    return redirect('/dashboard')



