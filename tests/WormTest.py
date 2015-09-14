
import unittest
from PyOpenWorm import *

class WormTest(unittest.TestCase):
    """Test for Worm."""

    def test_get_network(self):
        w = Worm()
        w.network(Network())
        self.assertIsInstance(Worm().get_neuron_network(), Network)

    def test_muscles1(self):
        w = Worm()
        w.cell(Muscle(name='MDL08'))
        w.cell(Muscle(name='MDL15'))
        self.assertIn(Muscle(name='MDL08'), list(Worm().muscles()))
        self.assertIn(Muscle(name='MDL15'), list(Worm().muscles()))


if __name__ == '__main__':
    unittest.main()
