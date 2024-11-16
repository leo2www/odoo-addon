#!/usr/bin/env python
# -*- coding:utf-8 -*-
{
    'name': 'estate',
    'depends': ['base'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'category': 'Sales',
    'summary': '房地产管理',
    'version': '1.0',
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ]
}