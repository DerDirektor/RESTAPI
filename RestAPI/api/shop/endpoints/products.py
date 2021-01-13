from flask import request
from flask_restplus import Resource
from RestAPI.api.myapi import api
from RestAPI.api.shop.api_definition import page_with_products, products

namespace = api.namespace('shop/products', description = ' Ops on')

# Routen über Klassen anlegen

@namespace.route('/')               # über Route API/shop--
class Offer(Resource):           # alles was man anbietet; Ressourcen werden angelegt


    @api.expect(pagination)                   # Produkt auslesen, pagination ist nicht identisch mit der aus 'api def'
    @api.marshal_with(page_with_product)
    def get(self):                  # get request, get  standard
        return products

    @api.expect(product)            # product in Datenbank anlegen
    def post(self):
        return None, 200
