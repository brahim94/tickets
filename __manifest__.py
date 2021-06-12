# -*- coding: utf-8 -*-
{
    'name': "tech_tickets",

    'description': """
        Etiquettes
    """,

    'author': "TECH-IT",
    'website': "http://www.tech-it.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'report/stock_picking_ticket.xml',
        'views/tickets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
