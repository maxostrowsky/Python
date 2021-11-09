# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database

DATABASE = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    # Now we use class methods to query our database
    @classmethod
    def create(cls, data:dict):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)'
        return connectToMySQL(DATABASE).query_db(query, data)

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def get_one(cls, data:dict):
        query = 'SELECT * FROM ninjas WHERE id=%(id)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    #u
    @classmethod
    def update_one(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, created_at=%(created_at)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    #d
    @classmethod
    def delete_one(cls,data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)
