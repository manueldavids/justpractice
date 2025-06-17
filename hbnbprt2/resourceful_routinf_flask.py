from flask import Flask, request
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app)

todos = {}

@api.route('/todo/<string:todo_id>')
class TodosSimple(Resource):
    def get(self, todo_id):
        if todo_id not in todos:
            return{'error': 'Todo not found' }, 404
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


if __name__ == '__main__':
    app.run(debug=True)

