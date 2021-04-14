# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
class Tarea(models.Model):
    
    _name = 'academy.tarea'
    _description = 'Tarea'
    
    tarea = fields.Char(string='Tarea')
    descripcion = fields.Char(string='Descripcion')
    tipoTarea = fields.Char(string='TipoTarea')
    horaInicio = datetime.strftime(fields.Datetime.now(), "%Y-%m-%d %H:%M:%S")
    horaFin = datetime.strftime(fields.Datetime.now(), "%Y-%m-%d %H:%M:%S")