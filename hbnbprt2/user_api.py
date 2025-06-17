from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace

""" Create Flask app """
app = Flask(__name__)
api = Api(app, version='1.0', title='User API')

""" Create a namespace """
ns = Namespace('users', description='User operations')
api.add_namespace(ns) 

""" Add the namespeace to the API """

""" Define the user model """
user_model = api.model('User', {
    'id': fields.Integer(readomly=True),
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='User email')
})

""" In memory storage """
users = {}
user_id = 1

""" Define the user model """
@ns.route('')
class UnderList(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        """ List all users """
        return list(users.values())

    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        """ Create a new user """
        global user_id
        data = request.json
        user = {
            'id': user_id,
            'name': data['name'],
            'email': data['email']
        }
        users[user_id] = user
        user_id += 1
        return user, 201

    @ns.route('/int:id>')
    @ns.response(404, 'User not found')
    @ns.param('id' 'The user identifier')
    class User(Resource):
        @ns.doc('get_user')
        @ns.marshal_with(user_model)
        def get(self, id):
            """ Get a user by 10 """
            if id not in users:
                api.abort(404, f"User {id} nor found")
            return users[id]
        
        @ns.doc('update_user')
        @ns.expect(user_model)
        @ns.marshal_with(user_model)
        def put(self, id):
            """ Update a user """
            if id not in users:
                api.abort(404, f"User {id} not found")
            data = request.json
            users[id].update(data)
            return users[id]

        @ns.doc('delete_user')
        @ns.response(204, 'User deleted')
        def delete(self, id):
            """ Delete a user """
            if id not in users:
                api.abort(404, f"User {id} not found")
            del users[id]
            return '', 204

if __name__ == '__main__':
    app.run(debug=True)
