from app import api
from app.controllers.api import ApiTodoController

api.add_resource(ApiTodoController.TodoController, '/todo', '/todo/<string:id>')

from app.controllers.api import ApiTodoController, ApiAuthController

api.add_resource(ApiAuthController.RegisterController, '/register')

api.add_resource(ApiAuthController.AuthController, '/login')