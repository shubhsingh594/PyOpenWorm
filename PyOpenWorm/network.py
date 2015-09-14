# -*- coding: utf-8 -*-
import PyOpenWorm as P
import rdflib as R

class Network():
    """A network of neurons
    """
    def __init__(self):
        self.connections = set()
        self.neurons = set()

    def connections(self):
        """
        Get all connections in the network

        :returns: A set of Connection objects
        :rtype: PyOpenWorm.Connection
        """
        return self.connections

    def neurons(self):
        """
        Get the set of neurons.

        :returns: A set of Neuron objects
        :rtype: PyOpenWorm.Neuron
        """
        return self.neurons

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
        for neuron in self.neurons:
            if neuron.name() == name:
                return neuron

    def sensory(self):
        """
        Get all sensory neurons

        :returns: A set of all sensory neurons
        :rtype: set(PyOpenWorm.Neuron)
        """
        out = set()
        for neuron in self.neurons:
            if neuron.type() == 'sensory':
                out.add(neuron)
        return out


    def interneurons(self):
        """
        Get all interneurons

        :returns: A list of all interneurons
        :rtype: set(PyOpenWorm.Neuron)
        """
        out = set()
        for neuron in self.neurons:
            if neuron.type() == 'interneuron':
                out.add(neuron)
        return out

    def motor(self):
        """
        Get all motor neurons

        :returns: A list of all motor neurons
        :rtype: set(PyOpenWorm.Neuron)
        """
        out = set()
        for neuron in self.neurons:
            if neuron.type() == 'motor':
                out.add(neuron)
        return out
