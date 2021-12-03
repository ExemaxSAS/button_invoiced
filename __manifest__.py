# -*- coding: utf-8 -*-
{
    'name': 'Change Invoice Status',
    'version': '14.0.1.0',
    'category': 'Extra Tools',
    'license': 'OPL-1',
    'summary' : 'Module that changes the state of "invoice_status" in Order Sale',
    'description': """
Module that changes the state of "invoice_status" in Order Sale
====================================

Module that changes the state of "invoice_status" in Order Sale
    """,
    'author' : 'Ivan Arriola',
    'website': 'https://www.exemax.com.ar/',
    'maintaner' : 'Exemax',    
    'depends': ['sale', 'account'],
    'data': [
        'views/sale_order.xml'
    ],
    'images': [
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}