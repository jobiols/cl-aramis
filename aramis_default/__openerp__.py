# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeo-soft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------

{
    'name': 'aramis',
    'version': '8.0.1.0',
    'category': 'Tools',
    'summary': 'Customización ARAMIS',
    'description': """

Customización ARAMIS Soluciones IT
==================================

""",
    'author': 'jeo Software',
    'depends': [
        'l10n_ar_base',  # modulo base para localización argentina
        'disable_openerp_online',  # elimina referencias a odoo online
        'account_cancel',  # Muestra el check en los diarios que permite cancelar asientos
        'hide_product_variants',  # oculta las variantes
        #'im_chat',  # mensajeria instantanea entre usuarios de odoo
        'invoice_order_by_id',  # ordena facturas ultima arriba
        #        'sale_order_recalculate_prices',  # agrega boton para recalcular precios
        #        'consult_product_price',    # consulta de precios
        #        'partner_search',            # permite buscar partners por varios criterios
        'account_journal_sequence',  # agrega un campo de secuencia en el diario para ordenarlos
        # 'account_statement_move_import'  # agrega boton de importar aputnes en extractos bancarios
        'l10n_ar_aeroo_sale',  # dependencia requerida
        'l10n_ar_aeroo_purchase',  # dependencia requerida
        'l10n_ar_aeroo_einvoice',  # dependencia requerida
        'l10n_ar_aeroo_stock',  # dependencia requerida
        'l10n_ar_aeroo_voucher',  # dependencia requerida
        'l10n_ar_states',
        'account_invoice_tax_add',  # agrega insercion manual de impuestos para factura de compras
        'product_unique_default_code',  # impide que se duplique el default_code
        'hide_messaging',  # oculta el menu de mensajeria
        'voucher_payment_check_fix',  # evita que aparezca cheques propios en medios de pago de cliente
        'account_invoice_tax_auto_update', # autocalcula los impuestos al salvar asi no hay que hacer el update
        'server_mode',  # disable some functions when running databases on odoo servers with parameter server_mode = "some value"
        #'account_transfer',  # permite hacer transferencia entre cuentas
        'web_export_view',   # reportes en excel de cualquier vista.
#        'currency_rate_update' # actualiza tipo de cambio

        #  Qplicaciones requeridas
        'sale',
        'purchase',
        'point_of_sale'

    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-sams', 'branch': '9.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '9.0'},

    ],
    'docker': [
        {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.5'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'}
    ]

}

