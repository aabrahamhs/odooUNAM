# -*- coding: utf-8 -*-
{
    'name':'Odoo Academy',
    'summary': """Academy App to Administrador de una biblioteca""",
    'description':"""Administrador de una bibliotea
        - Libros
        - Clientes
        - Alquileres
    """,
    'author':'aabrahamhs',
    'website':'https://www.odoo.com',
    'category':'Training',
    'version':'0.1',
    'depends':['base'],
    'data':[
        'security/biblioteca_security.xml',
        'security/ir.model.access.csv',
        'views/biblioteca_menuitems.xml',
        'views/libro_views.xml',
    ],
    'demo':[
        'demo/libro_demo.xml',
    ],
}