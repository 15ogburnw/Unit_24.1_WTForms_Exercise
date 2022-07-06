from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, request, redirect, render_template, flash
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def home():
    """View function for the adoption home page. Renders a list of all pets"""

    pets = Pet.query.all()

    return render_template('all_pets.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet_form():
    """View function for route to add a pet. Renders an AddPetForm and validates its submission"""

    form = AddPetForm()

    # If form submission is valid on a post request, pet is added to the database. If not, the form is reloaded. For a get request, it renders the html template

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data

        if form.photo_url.data:
            photo_url = form.photo_url.data
        else:
            photo_url = None

        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """View function for pet details page. Also includes a form to edit pet's photo, notes, and availability and validates its submission"""

    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)

    # If form submission is valid on a post request, pet is updated in the database. If not, the page is reloaded. If it is a get request, it renders the html template

    if form.validate_on_submit():

        available = form.available.data
        notes = form.notes.data

        if form.photo_url.data:
            photo_url = form.photo_url.data
        else:
            photo_url = None

        pet.available = available
        pet.notes = notes
        pet.photo_url = photo_url

        db.session.add(pet)
        db.session.commit()

        return redirect(f'/{pet_id}')

    else:
        return render_template('pet_details.html', form=form, pet=pet)
