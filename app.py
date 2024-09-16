from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
from flask_migrate import Migrate
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "very-secret"

connect_db(app)

# Flask-Migrate setup
migrate = Migrate(app, db)

@app.route("/")
def display_homepage():
    """Render the homepage."""
    return render_template("index.html")


@app.route("/api/cupcakes", methods=["GET"])
def retrieve_all_cupcakes():
    """Retrieve all cupcakes from the database."""
    cupcakes = [cupcake.serialize_cupcake() for cupcake in Cupcake.query.all()]
    return jsonify(format_response("cupcakes", cupcakes))


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["GET"])
def retrieve_single_cupcake(cupcake_id):
    """Retrieve a single cupcake by ID."""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(format_response("cupcake", cupcake.serialize_cupcake()))


@app.route("/api/cupcakes", methods=["POST"])
def add_new_cupcake():
    """Add a new cupcake."""
    data = request.json

    new_cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data.get('image') or DEFAULT_IMAGE
    )

    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(format_response("cupcake", new_cupcake.serialize_cupcake())), 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def modify_cupcake(cupcake_id):
    """Update cupcake data."""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    data = request.json

    cupcake.flavor = data.get("flavor", cupcake.flavor)
    cupcake.size = data.get("size", cupcake.size)
    cupcake.rating = data.get("rating", cupcake.rating)
    cupcake.image = data.get("image", cupcake.image)

    db.session.commit()

    return jsonify(format_response("cupcake", cupcake.serialize_cupcake()))


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete a cupcake."""
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(format_response("message", "Cupcake deleted"))


def format_response(key, data):
    """Helper function to standardize JSON responses."""
    return {key: data}
