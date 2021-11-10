# _*_ coding: utf-8  _*_
{
    'name': 'Odoo Academy',
    'sumary': 'Academy app to manage training',
    'description': """
       Academy app to manage training
       - Courses
       - Sessions
       - Atendees
    """,
    'author': 'ST4B',
    'website': 'http://www.st4business.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
        #'demo/academy.demo.xml'
    ],
    'license': 'LGPL-3'
}