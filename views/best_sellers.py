from flask_restx import Resource

from api_config import api

best_sellers_namespace = api.namespace(
    'mais_vendidos', description='List all orders'
)


@best_sellers_namespace.route('/')
class BestSellersView(Resource):
    def get(self):
        # TODO: Listar os produtos mais vendidos em ordem decrescente
        ...
