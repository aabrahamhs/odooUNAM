# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError

class Libro(models.Model):
    
    _name = 'academy.libro'
    _description = 'Libro'
    
    nombre = fields.Char(string='Nombre')
    autor = fields.Char(string='Autor')
    editor = fields.Char(string='Editor')
    editorial = fields.Char(string='Editorial')
    anioEdicion = fields.Integer(string='anioEdicion')
    isbn = fields.Char(string='Isbn')
    genero = fields.Char(string='Genero')
    
    @api.onchange('isbn')
    def _valida_isbn(self):
        if len(self.isbn) != 13:
            raise ValidationError('El isbn debe ser de 13 caracteres')