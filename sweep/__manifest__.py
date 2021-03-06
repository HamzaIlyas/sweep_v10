{
    'name': 'Sweep',
    'version': '1.0',
    'summary': 'Sweep Module',
    'description':
        """
        This module helps an organization to manage its sweep products with separate analytic account. 
        """,
    'category': 'Accounting',
    'author': 'Hamza Ilyas',
    'website': 'hamza.ilyaaaas@gmail.com',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'data/scheduler.xml',
        'security/ir.model.access.csv',
        'wizard/sweep_process_wizard.xml',
        'views/view.xml',
        # 'views/credit_application_sequence.xml',
    ],
    'installable': True,
    'auto_install': False,
}