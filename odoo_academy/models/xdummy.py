from odoo import models, fields, api

class Xdummy(models.Model):
    _name = "academy.idummy"
    _description = 'Dummy Info'
    
    name = fields.Char(string='Titulo', required=True)
    description = fields.Text(string='Descripcion')
    level = fields.Selection(string='Nivel', 
                             selection=[('principiante', 'Principiante'),
                                       ('intermedio', 'Intermedio'),
                                       ('avanzado','Avanzado')],
                             copy=False)
    activo = fields.Boolean(string='Activo', default=True)