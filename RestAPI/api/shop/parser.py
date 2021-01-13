from flask_restplus import reqparse

pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument('page', type = int, required = False, default= 1, help= 'page number')
pagination_parser.add_argument('items_per_page', type = int, default= 10,
                               choices =[10,20,50], help= 'item per page')