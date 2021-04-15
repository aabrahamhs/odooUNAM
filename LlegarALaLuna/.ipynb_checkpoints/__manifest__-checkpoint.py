# -*- coding: utf-8 -*-

{
    'name':'Odoo Academy',
    'summary': """Academy App to Llegar a la Luna""",
    'description':"""Modulo de odoo inc. para llegar a la luna
        - Nave espacial
        - Tripulacion
    """,
    'author':'aabrahamhs',
    'website':'https://www.odoo.com',
    'category':'Training',
    'version':'0.1',
    'depends':['base'],
    'data':[
        'security/academy_nave_security.xml',
        'security/ir.model.access.csv',
        'views/espacio_menuitems.xml',
        'views/nave_views.xml'
    ],
    'demo':[
        'demo/naveEspacial_demo.xml',
    ],
}