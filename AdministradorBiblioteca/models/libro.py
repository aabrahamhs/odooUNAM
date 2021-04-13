# -*- coding: utf-8 -*-

from odoo import models, fields, api

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