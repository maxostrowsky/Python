from flask_app import app
from flask_app.controllers import controller_users, controller_recipes

# make sure this is at the bottom of your server.py file
if __name__=="__main__":
    app.run(debug=True)