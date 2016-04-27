# -*- coding: utf-8 -*-
from openerp import models, fields, api


class RutaEmpleado(models.Model):
    _name = 'ruta.empleado'
    _description = 'Empleados para la hoja de ruta'
    name = fields.Char('Nombre')
