# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError

class NaveEspacial(models.Model):
    
    _name = 'academy.nave_espacial'
    _description = 'Nave Espacial'
    
    mision_id = fields.Many2one(comodel_name='academy.mision',string='Mision',ondelete='cascade')
    
    nombre=fields.Char(string='Nombre')
    alto = fields.Integer(string='Alto')
    ancho = fields.Integer(string='Ancho')
    largo = fields.Integer(string='Largo')
    
    tipoCombustible = fields.Char(string='TipoCombustible')
    tipoBarco = fields.Char(string='TipoBarco')
    nopasajeros = fields.Integer(string='Nopasajeros')
    
    cantidad_combustible=fields.Integer(string='cantidad_combustible')
    no_motores=fields.Integer(string='no_motores')
    no_caracteristicas_seguridad=fields.Integer(string='no_caracteristicas_seguridad')
    
    active = fields.Boolean(string='Active', default=True)
    
    @api.constrains('ancho','largo')
    def _valida_tamanio(self):
        for record in self:
            if record.largo <= record.ancho:
                raise UserError("El ancho no puede ser mayor que el largo")
    
    
    