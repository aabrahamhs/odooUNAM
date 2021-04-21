# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError

class Alquiler(models.Model):
    
    _name = 'academy.alquiler'
    _description = 'Alquiler'
    
    nombre_alquiler = fields.Char(string='Nombre Alquiler')
    
    libro_ids=fields.One2many(comodel_name='academy.libro',inverse_name='libro_id',string='Libros')
    
    cliente_id=fields.Many2one(comodel_name='res.partner',string='Cliente')