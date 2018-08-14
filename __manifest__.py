# -*- coding: utf-8 -*-
{
    'name': 'Preview Reports and PDF Attachments in Browser. Open Report or PDF Attachment in new tab instead of downloading',
    'version': '11.0.1.0',
    'author': 'Ivan Sokolov',
    'category': 'Productivity',
    'license': 'GPL-3',
    'website': 'https://demo.promintek.com',
    'description': """
    Preview reports and pdf attachments in browser instead of downloading them              
""",
    'depends': ['base', 'web'],

    'data': [
        'views/prt_report_preview_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
