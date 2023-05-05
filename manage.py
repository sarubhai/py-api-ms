from flask.cli import FlaskGroup

from ms import create_app, db
from ms.models.product import Product
from ms.models.customer import Customer


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(Product(
        name='Baseball Caps',
        uom='Piece',
        quantity=20,
        price=9.99,
        in_stock=True
    ))
    db.session.add(Product(
        name='Henley Shirts',
        uom='Piece',
        quantity=50,
        price=28.75,
        in_stock=True
    ))
    db.session.add(Product(
        name='Shorts',
        uom='Pairs',
        quantity=250,
        price=17.99,
        in_stock=True
    ))
    db.session.add(Product(
        name='Sweaters',
        uom='Piece',
        quantity=0,
        price=19.99,
        in_stock=False
    ))
    db.session.add(Product(
        name='Socks',
        uom='Pairs',
        quantity=210,
        price=8.99,
        in_stock=True
    ))

    db.session.add(Customer(
        name='John Doe',
        dob='1990-01-01',
        address='Alexzandraplatz, 10153'
    ))
    db.session.add(Customer(
        name='Jane Doe',
        dob='1992-02-15',
        address='Hermanstrasse, 11967'
    ))

    db.session.commit()


if __name__ == '__main__':
    cli()