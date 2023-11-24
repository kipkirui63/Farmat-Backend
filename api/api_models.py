from api import fields, api, ma, CartItem
from marshmallow import Schema, fields
from flask_restx import Api,Resource,Namespace,fields

ns = Namespace('farmart')
api.add_namespace(ns)

# ------------------------- A P I _ M O D E L S ------------------------

users_summary_schema = api.model('users',{
    "public_id": fields.String,
    "username": fields.String,
    "email": fields.String,
    "profile_pic": fields.String
    
})

users_schema = api.model('users',{
    "public_id": fields.String,
    "username": fields.String,
    "email": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "address": fields.String,
    "phone_number": fields.String,
    "profile_pic": fields.String,
})




user_input_schema = api.model('user_input',{
    "username": fields.String,
    "password": fields.String,
    "repeatpassword": fields.String,
    "email": fields.String,
    "profile_pic": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "address": fields.String,
    "phone_number": fields.String,
})

signup_input_schema = api.model('signup_input',{
    "username": fields.String,
    "password": fields.String,
    "repeatpassword": fields.String,
    "email": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    
})

user_login_schema = api.model('user_login',{
    "username": fields.String,
    "password": fields.String,

})

category_input_schema = api.model('category_input',{
    "name": fields.String,
    'image': fields.String
})












































