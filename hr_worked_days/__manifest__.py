# -*- coding: utf-8 -*-
{
    'name': "Dosttech Payslip Customizations",

    'summary': """
        Calculate working days excluding leaves in payslip""",

    'description': """
        Calculation of working days
        Calculates the number of working days for a selected month in the payslip calculation.
        Some use cases where this module can be useful:
            *an employee hasn't worked the whole month and his basic pay needs to be prorated
        based on the actual worked days out of total worked days
            *use working days information for calculation in any other salary rule
        
        A float field has been added to the payslip form view which is calculating the working 
        days in respective working schedule of an employee by talking out the respective global
        leaves.
        
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
