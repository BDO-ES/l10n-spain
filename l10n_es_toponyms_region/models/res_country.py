# -*- coding: utf-8 -*-
# Copyright 2020 Janire Olaguibel <janire.olaguibel@bdo.es>
# Copyright 2011-2012 Iker Coranti (www.avanzosc.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
                                                                                             
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    region_id = fields.Many2one('res.country.region', 'Region', domain="[('country_id', '=', country_id)]")

    @api.onchange('zip_id')
    def onchange_zip_id(self):
        super(ResPartner, self).onchange_zip_id()
        for partner in self:
            if (partner.zip_id and partner.zip_id.state_id and
                    partner.zip_id.state_id.region_id):
                partner.region_id = partner.zip_id.state_id.region_id.id

class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    region_id = fields.Many2one('res.country.region', 'Region')


class ResCountryRegion(models.Model):
    _name = 'res.country.region'
    _description = 'Region'
    _order = 'name'

    code = fields.Char('Code', size=10)
    name = fields.Char('Name', size=64, required=True)
    country_id = fields.Many2one('res.country', 'Country', required=True)