# -*- coding: utf-8 -*-
from .muscle import Muscle
from .cell import Cell
from .network import Network


class Worm():
    """
    A representation of the whole worm.

    All worms with the same name are considered to be the same object.
    """
    def __init__(self):
        self.network = Network()
        self.cells = set()

    def network(self, n=None):
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
        if n != None:
            self.network = n
        return self.network

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
        out = set()
        for cell in cells:
            if cell isinstance Muscle:
                out.add(cell)
        return out

    def cell(self, cell_obj):
        """
        Add a cell object to the worm

        Example::

            >>> P.Worm().cell(Muscle(name=='PM1D'))
        """
        if (cell_obj isinstance Cell) == False:
            raise InputError("Must include an object that is a Cell or a subclass")
        cells.add(cell_obj)
