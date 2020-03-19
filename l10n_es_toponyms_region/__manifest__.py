# -*- coding: utf-8 -*-
# Copyright 2020 Janire Olaguibel <janire.olaguibel@bdo.es>
# Copyright 2011-2012 Iker Coranti (www.avanzosc.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Comunidades Autónomas de España",
    "version": "12.0.1.0.0",
    "author": "Spanish Localization Team, "
              "ZikZakMedia, "
              "BDO, "
              "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-spain",
    "category": "Localization",
    "depends": [
        "base_location_geonames_import",
        "contacts"
    ],
    "license": "AGPL-3",
    "data": [
        # "wizard/l10n_es_toponyms_wizard.xml",
        "views/res_country_region_view.xml",
        "security/ir.model.access.csv",
    ],
    'installable': True,
}
