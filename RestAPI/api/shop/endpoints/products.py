from flask import request
from flask_restplus import Resource
from RestAPI.api.myapi import api
from RestAPI.api.shop.api_definition import page_with_products, product
from RestAPI.api.shop.parser import pagination_parser as pagination

namespace = api.namespace('shop/products', description = ' Ops on')

# Routen über Klassen anlegen

@namespace.route('/')               # über Route API/shop--
class Offer(Resource):           # alles was man anbietet; Ressourcen werden angelegt


    @api.expect(pagination)                   # Produkt auslesen, pagination ist nicht identisch mit der aus 'api def'
    @api.marshal_with(page_with_product)
    def get(self):                  # get request, get  standard
        args = pagination.parse_args(request)
        page = args.get('page',1)
        items_per_page = args.get('item_per_page',10)
        return products

    @api.expect(product)            # product in Datenbank anlegen
    def post(self):
        return None, 200
