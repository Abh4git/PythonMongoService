from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import Document, StringField, IntField, EmbeddedDocument, EmbeddedDocumentField
from dataclasses import dataclass
import json

@dataclass
class ProductDetail(EmbeddedDocument):
    """ Product Model for storing Product related details """
    title:str
    productinfo:str


    productdetail = StringField(max_length=10000,required=True)

    def __init__(self, productdetail,*args, **kwargs):
         super(EmbeddedDocument,self).__init__(*args, **kwargs)
         self.productdetail=productdetail


    def __repr__(self):
        return "<ProductDetail '{}'>".format(self.productdetail)

    def to_json(self):
        return "{ productdetail:" + str(self.productdetail) + "}"

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

@dataclass
class Product(Document):
    """ Product Model for storing Product related details """
    id:int
    title:str
    productdetail:str

    id = IntField(primary_key=True)
    title = StringField(max_length=255,required=True)
    productdetail = EmbeddedDocumentField(ProductDetail)

    def __init__(self, id, title, productdetail,*args, **kwargs):
         super(Document,self).__init__(*args, **kwargs)
         self.id=id
         self.title=title
         self.productdetail=productdetail


    def __repr__(self):
        return "<Product '{}'>".format(self.title)

    def to_json(self):
        return "{ id:" + str(self.id) + ", title:" + self.title +",productdetail:" + self.productdetail + "}"

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
