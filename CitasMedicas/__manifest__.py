# -*- coding: utf-8 -*-
{
    'name': "Gestión de Citas Médicas",

    'summary': "Control de citas médicas",

    'description': """
        Módulo para el control de citas médicas
    """,

    'author': "JoseLuisLopezGonzalez",
    'website': "http://www.4157490.com",

    'category': 'Healthcare',
    'version': '1.0',

    'depends': [
        'base', 
        'contacts',
        'calendar',
    ],

    'data': [
        'security/medical_appointment_security.xml',
        'security/ir.model.access.csv',
        'views/medical_appointment_views.xml',
        'report/medical_appointment_report.xml',
        'data/medical_appointment_data.xml',
    ],

    'application': True,
}