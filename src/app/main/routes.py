#All Routes are defined here
from flask_cors import CORS, cross_origin
from app.main.controller.products import ProductController
from flask import request, jsonify
import json
#Test route without any connections
def test():
    return "{testroutesuccess:'Test Route Success!'}"

api_v2_cors_config = {
  "origins": [
    'http://localhost:3000'  # React
  # React
  ],
  "methods": ["OPTIONS", "GET", "POST"],
  "allow_headers": ["Authorization", "Content-Type"]
}

#route returning Products list
@cross_origin(**api_v2_cors_config)
def getProductsList():
    productC = ProductController()
    return productC.getAllProducts()

#route for products list filtered by product types
@cross_origin(**api_v2_cors_config)
def addProduct():
    body = request.get_json()
    productController = ProductController()
    print (body['productdetail'])
    newproduct=productController.addProduct(body['id'], body['title'],body['productdetail'])
    return jsonify(newproduct), 201
