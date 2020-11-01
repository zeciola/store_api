from typing import NewType, Dict

from database_config import db
from models.order import Order
from models.order_item import OrderItem
from models.product import Product

OrderModel = NewType('OrderModel', Order)
ProductModel = NewType('ProductModel', Product)


class OrderDTO:

    def __save_changes(self, data: OrderModel) -> None:
        """
        Save model on database.

        Parameters
        ----------
        data: Order
            Model object.

        """
        db.session.add(data)
        db.session.commit()

    def create_order(self, order: dict) -> OrderModel:
        """
        Create a order on database.

        Parameters
        ----------
        order: dict
            Serialized order payload.

            Payload
            -------
            product_id: int
                Product identifier.
            total: float
                Value to pay on order
            amount: int
                Amount of product
        Returns
        -------
        order_model: Order

        """

        order_item = {}
        order_item['product_id'] = order.pop('product_id')
        order_item['amount'] = order.pop('amount')

        order_model = Order(**order)
        self.__save_changes(order_model)

        order_item['order_id'] = order_model.id
        order_item_model = OrderItem(**order_item)

        self.__save_changes(order_item_model)

        return {'order': order_model, 'order_item': order_item_model}

    def get_order(self, id: int) -> Dict[str, OrderModel]:
        """
        Get a order from database.

        Parameters
        ----------
        id: int
            Order identifier.

        Returns
        -------
        order_model: Order
            Model object from database.

        """
        order_model = Order.query.get(id)
        return order_model

    def all_orders(self) -> Dict[str, list]:
        """
        Get all order from database.

        Returns
        -------
        dict
            Dictionary of orders list.

        """
        orders_list = Order.query.all()
        return {'orders': orders_list}


class ProductDTO:

    def __save_changes(self, data: ProductModel) -> None:
        """
        Save model on database.

        Parameters
        ----------
        data: Order
            Model object.

        """
        db.session.add(data)
        db.session.commit()

    def create_product(self, product: dict) -> ProductModel:
        """
        Create a new product on database.

        Parameters
        ----------
        product: dict
             Serialized product payload.

        Returns
        -------
        product: Product
            Created model object.

        """
        product_model = Product(**product)
        self.__save_changes(product_model)
        return product

    def all_products(self) -> ProductModel:
        """
        List all products from database.

        Returns
        -------
        dict
            Dictionary of product list.

        """
        products_list = Product.query.all()
        return products_list

    def update_product(self, id: int, product: dict) -> ProductModel:
        """
        Update a specific product on database.

        Parameters
        ----------
        id: int
            Product identifier.
        product: dict
            Serialized product payload.

        Returns
        -------
        product_model: Product
            Updated model object.

        """
        product_model = Product.query.get(id)
        product_model(**product)
        self.__save_changes(product_model)
        return product_model
