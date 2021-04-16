# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
class Tarea(models.Model):
    
    _name = 'academy.tarea'
    _description = 'Tarea'
    
    tarea = fields.Char(string='Tarea')
    descripcion = fields.Char(string='Descripcion')
    tipoTarea = fields.Char(string='TipoTarea')
    lider=fields.Char(string='Lider')
    estado = fields.Selection(string='Estado',
                            selection=[('borrador','Borrador'),
                                       ('listo','Listo'),
                                       ('enprogreso','En progreso'),
                                      ('terminado','Terminado')],
                            copy=False)
    horaInicio = datetime.strftime(fields.Datetime.now(), "%Y-%m-%d %H:%M:%S")
    horaFin = datetime.strftime(fields.Datetime.now(), "%Y-%m-%d %H:%M:%S")
    
    @api.onchange('lider')
    def _pasar_estado_a_listo(self):
        if len(self.lider) > 0 :
            estado = 'listo'