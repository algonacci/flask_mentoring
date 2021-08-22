from app.controllers.MyViewController import MyViewController
from app import api, web
from app.controllers import MyController, MyViewController, ParameterController

api.add_resource(MyController.MyController, '/')

web.add_resource(MyViewController.MyViewController, '/')

web.add_resource(MyViewController.MySecondViewController, '/say-my-name')

web.add_resource(ParameterController.ParameterController, '/latihan-parameter')