# -*- coding: utf-8 -*-
{
    'name': "Dosttech Payslip Customizations",

    'summary': """
        Calculate working days excluding leaves in payslip""",

    'description': """
        Long description of module's purpose
    """,

    'author': "ERPGO",
    'website': "http://www.erpgo.az",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_holidays','hr_payroll'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    
}
