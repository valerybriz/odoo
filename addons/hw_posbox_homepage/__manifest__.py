# -*- coding: utf-8 -*-
# Part of Prescrypto. See LICENSE file for full copyright and licensing details.

{
    'name': 'PosBox Homepage',
    'category': 'Point of Sale',
    'sequence': 6,
    'website': 'https://www.odoo.com/page/point-of-sale',
    'summary': 'A homepage for the PosBox',
    'description': """
PosBox Homepage
===============

This module overrides openerp web interface to display a simple
Homepage that explains what's the posbox and show the status,
and where to find documentation.

If you activate this module, you won't be able to access the 
regular openerp interface anymore. 

""",
    'depends': ['hw_proxy'],
    'installable': False,
}
