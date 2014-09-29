# -*- encoding: utf-8 -*-
############################################################################
#    Module Writen to OpenERP, Open Source Management Solution             #
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).            #
#    All Rights Reserved                                                   #
# Credits######################################################
#    Coded by: author NAME LASTNAME <email@openerp.com.ve>                 #
#    Planified by: Nhomar Hernandez                                        #
#    Finance by: COMPANY NAME <EMAIL-COMPANY>                              #
#    Audited by: Humberto Arocha humberto@openerp.com.ve                   #
############################################################################
#    This program is free software: you can redistribute it and/or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation, either version 3 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>. #
############################################################################

from openerp.osv import fields, osv



class invoice_multicompany_report(osv.Model):
    """
    invoice_multicompany_report
    """

    _inherit = 'res.company'
    _columns = {
        'purchase_report_id': fields.many2one('ir.actions.report.xml', 'Purchase Report', required=False, domain="[('model','=','purchase.order')]"),
        'purchase_request_id': fields.many2one('ir.actions.report.xml', 'Purchase Request', required=False, domain="[('model','=','purchase.order')]"),
    }
