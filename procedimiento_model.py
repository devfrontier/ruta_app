# -*- coding: utf-8 -*-
from openerp import models, fields, api


class RutaProcedimiento(models.Model):
    _name = 'ruta.procedimiento'
    _description = 'Tipos de Procedimientos'
    name = fields.Char('Descripción')
