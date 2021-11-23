# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from . import models

from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    # Create QC triggers
    env = api.Environment(cr, SUPERUSER_ID, {})
    langs = env['res.lang'].sudo().get_installed()
    for lang in langs:
        if 'zh_CN' in lang:
            pdone = env['ir.translation'].sudo().search([('name', '=', 'qc.trigger,name'),
                                                         ('res_id', '=', env.ref('quality_control_mrp_oca.qc_trigger_mrp').id),
                                                         ('lang', '=', 'zh_CN'),
                                                         ('src', '=', 'Production done')
                                                         ])
            if pdone:
                pdone.write({'value': '生产完工',
                             'state': 'translated'})
            else:
                env['ir.translation'].sudo().create({'name': 'qc.trigger,name',
                                                 'res_id': env.ref('quality_control_mrp_oca.qc_trigger_mrp'),
                                                 'lang': 'zh_CN',
                                                 'type': 'model',
                                                 'src': 'Production done',
                                                 'value': '生产完工',
                                                 'state': 'translated',
                                                 'module': 'quality_control_oca'})
            break
