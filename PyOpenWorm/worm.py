# -*- coding: utf-8 -*-
from .dataObject import DataObject
from .muscle import Muscle
from .cell import Cell
from .network import Network


class Worm():
    """
    A representation of the whole worm.

    All worms with the same name are considered to be the same object.
    """

    def network(self):
        """
        Return the neuron network of the worm.

        Example::

            # Grabs the representation of the neuronal network
            >>> net = P.Worm().network()

            # Grab a specific neuron
            >>> aval = net.aneuron('AVAL')

            >>> aval.type()
            set([u'interneuron'])

            #show how many connections go out of AVAL
            >>> aval.connection.count('pre')
            77

        :returns: An object to work with the network of the worm
        :rtype: PyOpenWorm.Network
        """
        return self.neuron_network()

    def muscles(self):
        """
        Get all Muscle objects attached to the Worm

        Returns a set of all muscles::

        Example::

            >>> muscles = P.Worm().muscles()
            >>> len(muscles)
            96

        :returns: A set of all muscles
        :rtype: set
         """

    def graph(self):
        """
         Get the underlying semantic network as an RDFLib Graph

        :returns: A semantic network containing information about the worm
        :rtype: rdflib.ConjunctiveGraph
         """

        return self.rdf
