from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):

    db.app = app
    db.init_app(app)


class Pet(db.Model):

    """
    Model for a pet at the adoption agency. 

    Includes info about the pet including name, species, age, notes, a photo of the pet, and its adoption availability.

    """

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, nullable=True,
                          default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA38G9S7aagUBfAbEOMRKJfPAdAoHpq8ulMw2NcS021UD7FdCcY4oH--vxNpMYrTF3HAQ&usqp=CAU')

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):

        return f'<Pet {self.name} the {self.species}>'
