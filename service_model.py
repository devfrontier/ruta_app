# -*- coding: utf-8 -*-
from openerp import models, fields, api


class RutaService(models.Model):
    _name = 'ruta.service'
    _description = 'Tipos de Servicios de Ruta'
    name = fields.Char('Descripción')