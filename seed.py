from app import app
from models import db, Cupcake

with app.app_context():
    db.drop_all()
    db.create_all()

    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    c3 = Cupcake(
        flavor="vanilla",
        size="medium",
        rating=8,
        image="https://cdn.vectorstock.com/i/1000x1000/33/11/one-cream-vanilla-cupcake-icon-vector-44533311.webp"
    )

    c4 = Cupcake(
        flavor="Chocolate",
        size="large",
        rating=9,
        image="https://i.fbcd.co/products/resized/resized-750-500/9cff85f80e3301e74bc59e8892da60a73e8fe33095018f823b52142833fe76b8.jpg"
    )

    db.session.add_all([c1, c2, c3, c4]) 
    db.session.commit()
