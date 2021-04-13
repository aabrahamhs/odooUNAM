# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class Tarea(models.Model):
    
    _name = 'academy.tarea'
    _description = 'Tarea'
    
    tarea = fields.Char(string='Tarea')
    descripcion = fields.Char(string='Descripcion')
    tipoTarea = fields.Char(string='TipoTarea')
    horaInicio = fields.Datetime.to_datetime(string ="HoraInicio", default=datetime.now())
    horaFin = fields.Datetime.to_datetime(string ="HoraFin", default=datetime.now())