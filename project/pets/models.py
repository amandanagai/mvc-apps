from project import db

class Pet(db.Model):
	__tablename__ = 'pets'

	id = db.Column(db.Integer, primary_key=True)
	pet_name = db.Column(db.Text)
	pet_age = db.Column(db.Integer)
	owner_id = db.Column(db.Integer, db.ForeignKey('owners.id', ondelete='cascade'))

	def __init__(self, pet_name, pet_age):
		self.pet_name = pet_name
		self.pet_age = pet_age