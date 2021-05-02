# -*- coding: utf-8 -*-

import unittest

from py4geo import settings

settings.DB_URI = "postgres://postgres:postgres@localhost/py4geotest"

from py4geo.setup import initdb

class PopulateTestCase(unittest.TestCase):

    def setUp(self):
        self.dbwiz = initdb()
        from py4geo.models import db
        from py4geo.setup.setup import modelsetup
        modelsetup()

    def test_populate(self):
        """ """

        from py4geo.models import db
        from py4geo.populate.tools import fetch_and_log_from_osm, Turbo

        lon, lat = 20.1486016, 46.2546312,

        base_query = {
            "query": [[{"k": "qwertyuiop", "modv": "not", "regv": "."},],],
            'distance': 1000,
        }

        query = Turbo.build_query(Turbo.optimize_centralized_query(
            lon, lat,
            [base_query]
        ), gtypes=['node', 'way', 'relation'])
        fetch_and_log_from_osm(query.encode())
        db.commit()

    def tearDown(self):
        import pdb; pdb.set_trace()
        self.dbwiz.destroy()

if __name__ == '__main__':
    unittest.main()
