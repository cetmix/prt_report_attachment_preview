# -*- coding: utf-8 -*-
{
    'name': 'Preview Reports and Attachments in Browser',
    'version': '11.0.1.0',
    'author': 'Ivan Sokolov',
    'category': 'Productivity',
    'license': 'GPL-3',
    'website': 'https://demo.promintek.com',
    'description': """
    Preview reports and attachments in browser instead of downloading them              
""",
    'depends': ['base', 'web'],

    'data': [
        'views/prt_report_preview_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
