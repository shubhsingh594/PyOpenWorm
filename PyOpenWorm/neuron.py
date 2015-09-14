import sqlite3
import sys
import PyOpenWorm as P
from PyOpenWorm import Cell


# XXX: Should we specify somewhere whether we have NetworkX or something else?

class Neuron(Cell):
    """
    A neuron.

    See what neurons express some neuropeptide

    Example::

        # Grabs the representation of the neuronal network
        >>> net = P.Worm().get_neuron_network()

        # Grab a specific neuron
        >>> aval = net.aneuron('AVAL')

        >>> aval.type()
        set([u'interneuron'])

        #show how many connections go out of AVAL
        >>> aval.connection.count('pre')
        77

        >>> aval.name()
        u'AVAL'

        #list all known receptors
        >>> sorted(aval.receptors())
        [u'GGR-3', u'GLR-1', u'GLR-2', u'GLR-4', u'GLR-5', u'NMR-1', u'NMR-2', u'UNC-8']

        #show how many chemical synapses go in and out of AVAL
        >>> aval.Syn_degree()
        90

    Parameters
    ----------
    name : string
        The name of the neuron.

    Attributes
    ----------
    type : DatatypeProperty
        The neuron type (i.e., sensory, interneuron, motor)
    receptor : DatatypeProperty
        The receptor types associated with this neuron
    innexin : DatatypeProperty
        Innexin types associated with this neuron
    neurotransmitter : DatatypeProperty
        Neurotransmitters associated with this neuron
    neuropeptide : DatatypeProperty
        Name of the gene corresponding to the neuropeptide produced by this neuron
    neighbor : Property
        Get neurons connected to this neuron if called with no arguments, or
        with arguments, state that neuronName is a neighbor of this Neuron
    connection : Property
        Get a set of Connection objects describing chemical synapses or gap
        junctions between this neuron and others

    """
    def __init__(self, name=False, **kwargs):
        Cell.__init__(self,name=name,**kwargs)
        # Get neurons connected to this neuron
        Neighbor(owner=self)
        # Get connections from this neuron
        Connection(owner=self)

        Neuron.DatatypeProperty("type",self, multiple=True)
        Neuron.DatatypeProperty("receptor", self, multiple=True)
        Neuron.DatatypeProperty("innexin", self, multiple=True)
        Neuron.DatatypeProperty("neurotransmitter", self, multiple=True)
        Neuron.DatatypeProperty("neuropeptide", self, multiple=True)
        ### Aliases ###
        self.get_neighbors = self.neighbor
        self.receptors = self.receptor

    def degree(self, type = 0):
        """Get the number of incoming and outgoing connections of this neuron.

        :param type: by default, provide incoming and outgoing for both
                     gap junctions and chemical synapses.  If 1, provide for only gap junctions.
                     If 2, provide for only chemical synapses.
        :returns: total number of incoming and outgoing connections
        :rtype: int
        """
        gjcount = 0
        for c in self.connection():
            if c.syntype.one() == 'gapJunction':
                gjcount += 1

        count = 0
        for c in self.connection.get('either'):
            if c.syntype.one() == 'send':
                count += 1

        if type == 0:
            return count + gjcount
        elif type == 1:
            return gjcount
        elif type == 2:
            return count

    def get_incidents(self, type=0):
        """ Get neurons which synapse at this neuron """
        # Directed graph. Getting accessible _from_ this node
        for item in self['nx'].in_edges_iter(self.name(),data=True):
            if 'GapJunction' in item[2]['synapse']:
                yield item[0]

    def __str__(self):
        n = self.name()
        if n is not None:
            return n
        else:
            return ""
