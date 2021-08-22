from flask import Flask # Memanggil library Flask
from flask_restful import Api #Memanggil library RESTful

app = Flask(__name__, template_folder='views') # Untuk menjelaskan nama modul yang digunakan, sehingga ketika folder lain memanggil folder app akan otomatis teridentifikasi.
api = Api(app, prefix='/api')
web = Api(app) #Melakukan inisialisasi terhadap library RESTful untuk route web



from app import routes # Memanggil file routes (akan segera dibuat)