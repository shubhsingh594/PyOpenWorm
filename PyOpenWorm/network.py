# -*- coding: utf-8 -*-
import PyOpenWorm as P
import rdflib as R

class Network():
    """A network of neurons
    """

    def connections(self):
        """
        Get all connections in the network

        :returns: A list of Connection objects
        :rtype: PyOpenWorm.Connection
        """

    def neuron(self, name):
        """
        Get a neuron by name.

        Example::

            # Grabs the representation of the neuronal network
            >>> net = P.Worm().network()

            # Grab a specific neuron
            >>> aval = net.neuron('AVAL')

            >>> aval.type()
            set([u'interneuron'])


        :param name: Name of a c. elegans neuron
        :returns: Neuron corresponding to the name given
        :rtype: PyOpenWorm.Neuron
        """

    def sensory(self):
        """
        Get all sensory neurons

        :returns: A list of all sensory neurons
        :rtype: list(Neuron)
        """

    def interneurons(self):
        """
        Get all interneurons

        :returns: A list of all interneurons
        :rtype: list(Neuron)
        """

    def motor(self):
        """
        Get all motor neurons

        :returns: A list of all motor neurons
        :rtype: list(Neuron)
        """
