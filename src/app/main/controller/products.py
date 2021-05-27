from app.main.model.products import Product, ProductDetail

from flask import  jsonify
import json
class ProductController:

    def __init__(self):
        pass

    def obj_dict(self,obj):
        return obj.to_json()

    def addProduct(self,id,title,productdetail):

        newproductdetail=ProductDetail(productdetail=json.dumps(productdetail))

        newProduct = Product(id=id,title=title,productdetail=newproductdetail)
        #newproductdetail.save()
        newProduct.save()
        return newProduct

    def getAllProducts(self):
        products=Product.query.all()
        return jsonify({"products":products})