# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course info'
    
    name = fields.Char(string='Title',required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level',
                            selection=[('beginner','Beginner'),
                                       ('intermediate','Intermediate'),
                                       ('advanced','Advanced')],
                            copy=False)
    active = fields.Boolean(string='Active', default=True)
    
    precio_base=fields.Float(string='Precio base', default=0.00)
    tarifa_adicional=fields.Float(string='Tarifa adicional', default=10.00)
    precio_total=fields.Float(string='Precio total', readonly=True)
    
    @api.onchange('precio_base','tarifa_adicional')
    def _onchange_precio_total(self):
        if self.precio_base < 0.0:
            raise UserError("precio base no puede ser negativo")
        self.precio_total=self.precio_base+self.tarifa_adicional
        
    @api.constrains('tarifa_adicional')
    def _checa_tarifa_adicional(self):
        for record in self:
            if record in self:
                if record.tarifa_adicional < 10.00:
                    raise ValidationError('Tarifa adicional no puede ser menor que %s' % record.tarifa_adicional )