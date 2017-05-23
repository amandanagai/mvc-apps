from flask import Blueprint, redirect, render_template, url_for, request
from project import db
from project.pets.forms import PetForm
from project.pets.models import Pet
from project.owners.models import Owner

pets_blueprint = Blueprint(
	'pets',
	__name__,
	template_folder='templates'
)

@pets_blueprint.route('/', methods=['GET', 'POST'])
def index(owner_id):
	owner = Owner.query.get(owner_id)
	if request.method == 'POST':
		form = PetForm(request.form)
		if form.validate():
			new_pet = Pet(request.form['pet_name'], request.form['pet_age'])
			new_pet.owner_id = owner_id
			db.session.add(new_pet)
			db.session.commit()
			return redirect(url_for('pets.index', owner_id=owner_id))
		return render_template('pets/new.html', owner_id=owner_id, form=form)
	return render_template('pets/index.html', owner=owner, pets=owner.pets)

@pets_blueprint.route('/new')
def new(owner_id):
	form = PetForm(request.form)
	return render_template('pets/new.html', owner_id=owner_id, form=form)

@pets_blueprint.route('/<int:id>/edit')
def edit(owner_id, id):
	pet = Pet.query.get(id)
	form = PetForm(obj=pet)
	return render_template('pets/edit.html', owner_id=owner_id, pet=pet, form=form)

@pets_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(owner_id, id):
	pet = Pet.query.get(id)
	if request.method == b'PATCH':
		form = PetForm(request.form)
		if form.validate():
			pet.pet_name = request.form['pet_name']
			pet.pet_age = request.form['pet_age']
			db.session.add(pet)
			db.session.commit()
			return redirect(url_for('pets.index', owner_id=owner_id))
		return render_template('pets/edit.html', owner_id=owner_id, id=id)
	if request.method == b'DELETE':
		db.session.delete(pet)
		db.session.commit()
		return redirect(url_for('pets.index', owner_id=owner_id))
	return render_template('pets/show.html', owner_id=owner_id, id=id, pet=pet)