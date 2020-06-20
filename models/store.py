from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    # returns a List of items that are in a given store
    items = db.relationship('ItemModel',
                            lazy='dynamic')  # do not create an object for every item that is inside this database

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in
                                             self.items.all()]}  # we  use .all() because of the lazy = "dynamic" above

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
