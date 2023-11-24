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



photo_category_schema = api.model('photo_category',{
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "price": fields.Integer,
    "image": fields.String,
})

transaction_schema = api.model('transaction', {
    "id": fields.Integer,
    "photo": fields.Nested(photo_category_schema),
    "user": fields.Nested(users_schema),
    "purchased_at": fields.DateTime,
})



category_schema = api.model('category',{
    "id": fields.Integer,
    "name": fields.String,
    "image": fields.String,
    "products": fields.List(fields.Nested(photo_category_schema))
})
categories_schema = api.model('categories',{
    "id": fields.Integer,
    "name": fields.String,
})



cart_item_input_schema = api.model('cart_item_input', {
    "product_id": fields.Integer,
    "quantity": fields.Integer,
    "cart_id": fields.Integer
    
})

transaction_input_schema = api.model('transaction_input', {
    "product_id": fields.Integer(required=True),
    "quantity": fields.Integer(required=True),
})


transaction_input_schema = api.model('transaction_input', {
    "id": fields.Integer,
})



carts_output_schema = api.model('carts_output',{
    "id": fields.Integer,
    "user_id":fields.Integer,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime

})

carts_input_schema = api.model('carts_input',{
    "id": fields.Integer,
    "user_id":fields.Integer,

})

vendor_input_schema = api.model('vendor_input',{
    "user_id" : fields.Integer, 
    "fullnames" :fields.String,
    "business_name" :fields.String,
    "mobile_number" :fields.String,
    "email_address" : fields.String,
    "physical_address" : fields.String,
    "latitude" : fields.Float,
    "longitude" : fields.Float,
    "product_list" : fields.String,
    "image" : fields.String,

})

vendors_schema=api.model('vendors',{
    "id":fields.Integer,
    "user_id" : fields.Integer,
    "fullnames" :fields.String,
    "business_name" :fields.String,
    "mobile_number" :fields.String,
    "email_address" : fields.String,
})































