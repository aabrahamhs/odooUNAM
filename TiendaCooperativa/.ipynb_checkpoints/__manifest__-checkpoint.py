# -*- coding: utf-8 -*-

{
    'name':'Odoo Academy',
    'summary': """Academy App to Tienda Cooperativa""",
    'description':"""Tienda Cooperativa
        - Voluntarios
        - Tienda
        - Productos
    """,
    'author':'aabrahamhs',
    'website':'https://www.odoo.com',
    'category':'Training',
    'version':'0.1',
    'depends':['base'],
    'data':[
        'security/tarea_security.xml',
        'security/ir.model.access.csv',
        'views/tarea_menuitems.xml',
        'views/tarea_views.xml'
    ],
    'demo':[
        'demo/tarea_demo.xml',
    ],
}