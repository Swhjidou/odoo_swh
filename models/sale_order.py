from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    h_id_utilisateur_confirme = fields.Many2one('res.users', string='Utilisateur confirmé', )

    # h_name = fields.Char(string="Nom et Prenom", required=True, )
    #
    #
    # def test_function(self):
    #     return