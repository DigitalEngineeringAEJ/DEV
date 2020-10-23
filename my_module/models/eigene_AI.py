#Schauen wir mal 

from odoo import models, fields, api


class my_module(models.Model):
     _name = 'my_module.my_AI'
     _description = 'my_module.my_AI'
     Anzahl_Infizierte = fields.Integer()
     Faktor = fields.Float()
     Population = fields.Integer()
     DX = fields.Float(compute="_calc_AI", store=True)
    
    
     @api.depends('DX')
     def _calc_AI(self):
         for record in self:
             record.DX = integer(record.Anzahl_Infizierte) * float(record.Faktor) / integer(record.Population)
    
    
    
    
