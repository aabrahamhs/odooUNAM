# -*- coding: utf-8 -*-

{
    'name':'Odoo Academy',
    'summary': """Academy App to manage Training""",
    'description':"""Academy module to manage Training
        - Courses
        - Sessions
        - Attendees
    """,
    'author':'aabrahamhs',
    'website':'https://www.odoo.com',
    'category':'Training',
    'version':'0.1',
    'depends':['base'],
    'data':[
        'views/course_views.xml',
    ],
    'demo':[
        'demo/academy_demo.xml',
    ],
}