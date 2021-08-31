from flask_jwt_extended.utils import create_refresh_token
from flask_restful import Resource
from flask import request
from datetime import timedelta
from app.models.user import User
from flask_jwt_extended import create_access_token, create_refresh_token

from app.response import response
from app.transformer.UserTransformer import UserTransformer
from werkzeug.security import generate_password_hash, check_password_hash


class RegisterController(Resource):
    def post(self):
        try:
            password = request.json['password']
            confirmation_password = request.json['confirmation_password']

            if password != confirmation_password: #Memvalidasi password harus sama
                raise Exception(
                    'Password and confirmation password do not match')

            check_user = User.objects(email=request.json['email']).first() 
            if check_user: #Memeriksa apakah user sudah terdaftar atau belum
                raise Exception('User already exists!')

            user = User()
            user.name = request.json['name']
            user.email = request.json['email']
            user.password = generate_password_hash(password) #Hashing password ke database
            user.save()

            payload = TokenGenerator(user).generate_access_token() #Generate token JWT

            return response.ok('User Registered!', payload)
        except Exception as e:
            return response.bad_request("{}".format(e), '')

class TokenGenerator(object):
    def __init__(self, user):
        self.user = user

    def generate_access_token(self):
        payload = {
            "id": str(self.user.id),
        } #Isi payload token

        access_token = create_access_token(
            identity=payload,
            fresh=True,
            expires_delta=timedelta(days=3)
        ) #Membuat access token


        refresh_token = create_refresh_token(
            identity=payload,
            expires_delta=timedelta(days=30)
        ) #Membuat refresh token

        self.user = UserTransformer.single_transform(self.user)

        self.user['token'] = {
            'access_token': access_token,
            'refresh_token': refresh_token
        } #Menambahkan access dan refresh token pada key token

        return self.user
    
    
class AuthController(Resource):
    def post(self):
        try:
            email = request.json['email']
            password = request.json['password']
            
            user = User.objects(email=email).first() #Periksa ke database

            if not user: #Apabila tidak ditemukan kita kembalikan pesan error
                raise Exception('Email or password is invalid!')
            

            if not check_password_hash(user.password, password): #Apabila password tidak sama, maka kembalikan pesan error
                raise Exception(
                    'Email or password is invalid!'
                )

            payload = TokenGenerator(user).generate_access_token() #Pembuatan token sama seperti registrasi
    
            return response.ok(f'Succesfully logged in, welcome {user.name}!', payload)
        except Exception as e:
            return response.bad_request("{}".format(e), '')
