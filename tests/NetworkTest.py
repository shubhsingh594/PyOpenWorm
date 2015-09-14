import PyOpenWorm, unittest

class NetworkTest(unittest.TestCase):
    def setUp(s):
        _DataTest.setUp(s)
        s.net = Network(conf=s.config)

    def test_aneuron(self):
        """
        Test that we can retrieve a Neuron by name.
        """
        self.assertTrue(isinstance(self.net.aneuron('AVAL'),PyOpenWorm.Neuron))

    def test_neurons(self):
        """
        Test that we can add arbitrary Neurons to the Network,
        and that they can be accessed afterwards.
        """
        self.net.neuron(Neuron(name='AVAL'))
        self.net.neuron(Neuron(name='DD5'))
        self.assertTrue('AVAL' in self.net.neuron_names())
        self.assertTrue('DD5' in self.net.neuron_names())

    def test_synapses_rdf(self):
        """ Check that synapses() returns connection objects """
        for x in self.net.synapse():
            self.assertIsInstance(x,Connection)
            break

if __name__ == '__main__':
    unittest.main()
