from ms import db

class Customer(db.Model):

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'dob': str(self.dob),
            'address': self.address,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }
    

    def add_customer(name, dob, address):
        customer = Customer(name=name, dob=dob, address=address)
        db.session.add(customer)
        db.session.commit()
        return Customer.to_json(customer)

    def get_all_customers():
        return [Customer.to_json(customer) for customer in Customer.query.all()]

    def get_customer_by_id(id):
        customer = Customer.query.filter_by(id=id).first()
        if customer is None:
            return None
        return Customer.to_json(customer)

    def update_customer(id, name, dob, address):
        customer = Customer.query.filter_by(id=id).first()
        if customer is None:
            return None
        
        customer.name = name
        customer.dob = dob
        customer.address = address
        db.session.commit()
        return Customer.to_json(customer)

    def delete_customer(id):
        Customer.query.filter_by(id=id).delete()
        db.session.commit()
