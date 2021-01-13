from flask_restplus import fields
from RestAPI.api.myapi import api


product= api.model('product', {
    'id': fields.Integer(readOnly = True, description = ' identifyer'),
    'name': fields.String(required =True ),
    #'category_id': fields.Integer(attribute='category.id'),
    #'category_name': fields.String(attribute = 'categroy.name'), # crossfield
})

catagroy = api.model('Product category',{
    'id': fields.Integer(readOnly=True, description = ' The ident pf category'),
    'name': fields.String(required = True)
})

pagination = api.model ('One page',{
    'page': fields.Integer(description = 'Current page'),
    'pages': fields.Integer(description= 'total pages'),
    'items_per_page': fields.Integer(description= 'Items per page'),
    'total_items': fields.Integer(description='Total amount of items')
})

#Sammlugn der Produkte
page_with_products = api.inherit('page with procucts', pagination,{
    'items': fields.List(fields.Nested(product))
})