# -*- coding: utf-8 -*-
{
    'name': "Analytic Accounts Improved",

    'summary': """ An improvement in Analyitic Accounts,
    by adding Graphics, filter, import/export automation and
    reports """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Eduweb group",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        "views/analytic_account_views.xml",
        "views/analytic_groups_views.xml",
        "data/reports.xml",
        "data/data_menu.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}