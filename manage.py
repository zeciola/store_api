from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from database_config import db
from models import order, order_item, product

from api_config import blueprint

from app import create_app
from utils.postman_collection import generate_postman_collection

app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def postman_collection():
    generate_postman_collection()


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
