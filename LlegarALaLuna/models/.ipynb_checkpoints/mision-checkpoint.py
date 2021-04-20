# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError
from datetime import datetime

class Mision(models.Model):
    
    _name = 'academy.mision'
    _description = 'Mision'
    
    descripcion=fields.Char(string='descripcion')
    nave_espacial=fields.One2many(comodel_name='academy.nave_espacial',inverse_name='mision_id',string='Nave espacial')
    '''fecha_lanzamiento = datetime.strftime(fields.Datetime.now(), "%Y-%m-%d %H:%M:%S")
    fecha_regreso = datetime.strftime(fields.Datetime.now(), "%Y-%m-%d %H:%M:%S")'''
    
    contactos_ids=fields.Many2many(comodel_name='res.partner',string='Contactos')