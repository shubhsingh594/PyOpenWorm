# -*- coding: utf-8 -*-

import unittest

import PyOpenWorm
import rdflib
from rdflib import plugin, Graph, Literal, URIRef
from rdflib.store import Store

class RDFLibTest(unittest.TestCase):
    """Tests RDFLib, our backend library that interfaces with the database as an
       RDF graph."""

    ident = URIRef("rdflib_test")
    uri = Literal("sqlite://")

    @classmethod
    def setUpClass(cls):
        cls.ns = {"ns1" : "http://example.org/"}

    def setUp(self):
        #This test uses an SQLAlchemy store with an sqlite backend
        store = plugin.get("SQLAlchemy", Store)(identifier=self.ident)
        self.graph = Graph(store, identifier=self.ident)
        self.graph.open(self.uri, create=True)

    def tearDown(self):
        self.graph.destroy(self.uri)
        try:
            self.graph.close()
        except:
            pass

    def test01(self):
        self.assert_(self.graph is not None)
        print(self.graph)

    def test_uriref_not_url(self):
        try:
            rdflib.URIRef("daniel@example.com")
        except:
            self.fail("Doesn't actually fail...which is weird")

    def test_uriref_not_id(self):
        """ Test that rdflib throws up a warning when we do something bad """
        #XXX: capture the logged warning
        import cStringIO
        import logging

        out = cStringIO.StringIO()
        logger = logging.getLogger()
        stream_handler = logging.StreamHandler(out)
        logger.addHandler(stream_handler)
        try:
            rdflib.URIRef("some random string")
        finally:
            logger.removeHandler(stream_handler)
        v = out.getvalue()
        out.close()
        self.assertRegexpMatches(str(v), r".*some random string.*")

    def test_BNode_equality1(self):
        a = rdflib.BNode("some random string")
        b = rdflib.BNode("some random string")
        self.assertEqual(a, b)

    def test_BNode_equality2(self):
        a = rdflib.BNode()
        b = rdflib.BNode()
        self.assertNotEqual(a, b)


if __name__ == '__main__':
    unittest.main()
