from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

from resources.user import UserRegister
from resources.item import ItemList, Item
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ghena'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()  # Creates  - 'sqlite:///data.db'


jwt = JWT(app, authenticate, identity)  # auth

# All endpoints
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items/')
api.add_resource(StoreList, '/stores/')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5001, debug=True)
