from flask_restful import Resource
from flask import request
from datetime import datetime
from app.models.todo import Todo
from flask_jwt_extended import jwt_required
from app.libraries.access_jwt import jwt_required

from app.response import response
from app.transformer.TodoTransformer import TodoTransformer


class TodoController(Resource):
    # @jwt_required()
    def get(self, id=None):
        if not id:
            todos = Todo.objects(deleted_at=None).all()
            todos = TodoTransformer.transform(todos)

        return response.ok('', todos)

    def post(self):
        try:
            todo = Todo()
            todo.title = request.json['title']
            todo.description = request.json['description']
            todo.save()

            return response.ok('Todo Created!', TodoTransformer.single_transform(todo))
        except Exception as e:
            return response.bad_request(e, '')
        
