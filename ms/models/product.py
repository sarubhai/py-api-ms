from ms import db

class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    uom = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(), nullable=False)
    in_stock = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name, uom, quantity, price, in_stock):
        self.name = name
        self.uom = uom
        self.quantity = quantity
        self.price = price
        self.in_stock = in_stock

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'uom': self.uom,
            'quantity': self.quantity,
            'price': self.price,
            'in_stock': self.in_stock,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }