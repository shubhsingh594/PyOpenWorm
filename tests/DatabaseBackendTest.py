# -*- coding: utf-8 -*-


class DatabaseBackendTest(unittest.TestCase):
    """Integration tests that ensure basic functioning of the database
      backend and connection.
    """

    def test_init_no_rdf_store(self):
        """ Should be able to init without these values """
        c = Configure()
        Configureable.conf = c
        d = Data()
        try:
            d.openDatabase()
        except:
            self.fail("Bad state")

    def test_ZODB_persistence(self):
        """ Should be able to init without these values """
        c = Configure()
        fname ='ZODB.fs'
        c['rdf.source'] = 'ZODB'
        c['rdf.store_conf'] = fname
        Configureable.conf = c
        d = Data()
        try:
            d.openDatabase()
            g = make_graph(20)
            for x in g:
                d['rdf.graph'].add(x)
            d.closeDatabase()

            d.openDatabase()
            self.assertEqual(20, len(list(d['rdf.graph'])))
            d.closeDatabase()
        except:
            traceback.print_exc()
            self.fail("Bad state")
        delete_zodb_data_store(fname)

    def test_trix_source(self):
        """ Test that we can load the datbase up from an XML file.
        """
        f = tempfile.mkstemp()

        c = Configure()
        c['rdf.source'] = 'trix'
        c['rdf.store'] = 'default'
        c['trix_location'] = f[1]

        with open(f[1],'w') as fo:
            fo.write(TD.TriX_data)

        connect(conf=c)
        c = config()

        try:
            g = c['rdf.graph']
            b = g.query("ASK { ?S ?P ?O }")
            for x in b:
                self.assertTrue(x)
        except ImportError:
            pass
        finally:
            disconnect()
        os.unlink(f[1])

    def test_trig_source(self):
        """ Test that we can load the datbase up from a trig file.
        """
        f = tempfile.mkstemp()

        c = Configure()
        c['rdf.source'] = 'serialization'
        c['rdf.serialization'] = f[1]
        c['rdf.serialization_format'] = 'trig'
        c['rdf.store'] = 'default'
        with open(f[1],'w') as fo:
            fo.write(TD.Trig_data)

        connect(conf=c)
        c = config()

        try:
            g = c['rdf.graph']
            b = g.query("ASK { ?S ?P ?O }")
            for x in b:
                self.assertTrue(x)
        except ImportError:
            pass
        finally:
            disconnect()

    def test_helpful_message_on_non_connection(self):
        """ The message should say something about connecting """
        Configureable.conf = False # Ensure that we are disconnected
        with self.assertRaisesRegexp(Exception, ".*[cC]onnect.*"):
            do = DataObject()


    USE_BINARY_DB = False
    BINARY_DB = "OpenWormData/worm.db"
    TEST_CONFIG = "tests/test_default.conf"
    try:
        import bsddb
        has_bsddb = True

    except ImportError:
        has_bsddb = False

    try:
        import numpy
        has_numpy = True
    except ImportError:
        has_numpy = False

    namespaces = { "rdf" : "http://www.w3.org/1999/02/22-rdf-syntax-ns#" }

    def clear_graph(graph):
        graph.update("CLEAR ALL")

    def make_graph(size=100):
        """ Make an rdflib graph """
        g = R.Graph()
        for i in range(size):
            s = rdflib.URIRef("http://somehost.com/s"+str(i))
            p = rdflib.URIRef("http://somehost.com/p"+str(i))
            o = rdflib.URIRef("http://somehost.com/o"+str(i))
            g.add((s,p,o))
        return g

    def delete_zodb_data_store(path):
        os.unlink(path)
        os.unlink(path + '.index')
        os.unlink(path + '.tmp')
        os.unlink(path + '.lock')

if __name__ == '__main__':
    unittest.main()
