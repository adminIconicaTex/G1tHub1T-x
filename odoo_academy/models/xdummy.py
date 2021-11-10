from odoo import models, fields, api

class Xdummy(models.Model):
    _name = "academy.idummy"
    _description = 'Dummy Info'
    
    nombre = fields.Char(string='Titulo', required=True)
    descripcion = fields.Text(string='Descripcion')
    nivel = fields.Selection(string='Nivel', 
                             selection=[('principiante', 'Principiante'),
                                       ('intermedio', 'Intermedio'),
                                       ('avanzado','Avanzado')],
                             copy=False)
    activo = fields.Boolean(string='Activo', default=True)