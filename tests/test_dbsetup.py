# -*- coding: utf-8 -*-

import unittest

from py4geo import settings

settings.DB_URI = "postgres://postgres:postgres@localhost/py4geotest"

from py4geo.setup import initdb

class SetupTestCase(unittest.TestCase):

    def test_dbsetup(self):
        wiz = initdb()

        from py4geo.setup.setup import modelsetup
        try:
            from py4geo.models import db
        except Exception as err:
            self.fail(err)
        else:
            modelsetup()

        wiz.destroy()

if __name__ == '__main__':
    unittest.main()
