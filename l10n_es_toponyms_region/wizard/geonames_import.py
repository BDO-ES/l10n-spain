# -*- coding: utf-8 -*-
# Copyright 2016 Davide Corio - Abstract srl
# Copyright 2017 Andrea Cometa - Apulia Software srl
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api

class CityZipGeonamesImport(models.TransientModel):
    _inherit = 'city.zip.geonames.import'

    @api.model
    def select_or_create_state(
        self, row, country_id, code_row_index=4, name_row_index=3
    ):
        res = super(better_zip_geonames_import, self).select_or_create_state(
            row, country_id, code_row_index=6, name_row_index=5)

        region_model = self.env['res.country.region']
        region = region_model.search([('code', '=', row[4])])
        if not region:
            region = region_model.create(
                {'code': row[4], 'name': row[3]})
        res.region_id = region.id
        return res


    def _create_regions(self, parsed_csv,
                       search_cities, max_import, state_dict):
        # Cities
        region_vals_list = []
        region_dict = {}
        for i, row in enumerate(parsed_csv):
            if max_import and i == max_import:
                break
            state_id = state_dict[row[self.code_row_index or 4]]
            region = self.select_region(
                row, self.country_id) if search_cities else False
            if not region:
                region_vals = self.prepare_region(
                    row, self.country_id, state_id)
                if region_vals not in region_vals_list:
                    region_vals_list.append(region_vals)
            else:
                region_dict[(region.name, state_id)] = region.id
        created_regions = self.env['res.country.region'].create(city_vals_list)
        for i, vals in enumerate(region_vals_list):
            region_dict[(vals['name'], vals['state_id'])] = created_regions[i].id
        return region_dict


    def _create_states(self, parsed_csv, search_states, max_import):
        # States
        state_vals_list = []
        state_dict = {}
        for i, row in enumerate(parsed_csv):
            if max_import and i == max_import:
                break
            state = self.select_state(row, self.country_id) if search_states else False
            if not state:
                state_vals = self.prepare_state(row, self.country_id)
                if state_vals not in state_vals_list:
                    state_vals_list.append(state_vals)
            else:
                state_dict[state.code] = state.id