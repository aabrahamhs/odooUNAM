# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError

import logging
_logger = logging.getLogger(__name__)

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
    
    libro_id = fields.Many2one(comodel_name='academy.alquiler',string='Alquiler',ondelete='cascade')
    
    @api.onchange('isbn')
    def _valida_isbn(self):
        for record in self:
            _logger.debug('Campo a verificar')
            _logger.debug(self)
            if self == True:
                continue
            else: 
                if len(self.isbn) != 13:
                    raise ValidationError('El isbn debe ser de 13 caracteres')
        