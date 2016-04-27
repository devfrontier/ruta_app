# -*- coding: utf-8 -*-
from openerp import models, fields, api

class RutaTask(models.Model):
    _name = 'ruta.task'
    _description = 'Servicios de Ruta'
    name = fields.Char('Descripción')
    fecha = fields.Datetime('Fecha')
    destino = fields.Char('Destino')
    cliente = fields.Many2one('res.partner')
    rubro = fields.Text()
    empleado = fields.Many2one('ruta.empleado')
    servicios = fields.Many2many(comodel_name='ruta.service')
    procedimientos = fields.Many2many (comodel_name='ruta.procedimiento')
    otro = fields.Char('Otro')
    is_done = fields.Boolean('Realizado?')
    nota = fields.Text()

    def onchange_cliente(self, cr, uid, ids, partner_id, context=None):
      res = {}
      if partner_id:
        obj = self.pool.get('res.partner').browse(cr, uid, partner_id)
        res['rubro'] = obj.category_id.name
      return {'value': res}

    @api.one
    def do_toggle_done(self):
        # print self.env.context
        self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
