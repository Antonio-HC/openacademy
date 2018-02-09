from odoo import api, models, fields, _

class Demo(models.Model):
	_name = 'openacademy.demo'

	name =fields.Char(string='Nombre', required=True)
	apellidos = fields.Char(string='Apellidos', required=False)
	sexo = fields.Char(string='Sexo', required=False)
	nacimeinto = fields.Date(default=fields.Date.today())
	edad = fields.Integer(string='Edad')

	_sql_contraints = [
		('name_description_check,CHECK(name != apellidos)',
		_("Campos iguales")),
		('name_unique','UNIQUE(name)',
		_("Nombre es unico"))
	]

