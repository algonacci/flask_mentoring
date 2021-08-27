from app import api
from app.controllers.api import ApiTodoController

api.add_resource(ApiTodoController.TodoController, '/todo', '/todo/<string:id>')