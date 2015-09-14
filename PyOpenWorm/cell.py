from PyOpenWorm import *
from string import Template
import neuroml
__all__ = [ "Cell" ]


class Cell():
    """
    A biological cell.

    All cells with the same name are considered to be the same object.

    Parameters
    -----------
    name : string
        The name of the cell
    lineageName : string
        The lineageName of the cell
        Example::

            >>> c = Cell(name="ADAL")
            >>> c.lineageName() # Returns ["AB plapaaaapp"]

    Attributes
    ----------
    name : DatatypeProperty
        The 'adult' name of the cell typically used by biologists when discussing C. elegans
    lineageName : DatatypeProperty
        The lineageName of the cell
    description : DatatypeProperty
        A description of the cell
    divisionVolume : DatatypeProperty
        When called with no argument, return the volume of the cell at division
        during development.

        When called with an argument, set the volume of the cell at division
        Example::

            >>> v = Quantity("600","(um)^3")
            >>> c = Cell(lineageName="AB plapaaaap")
            >>> c.divisionVolume(v)
    """
    def __init__(self, name=False, lineageName=False, **kwargs):
        #DataObject.__init__(self,**kwargs)

        #Cell.DatatypeProperty('lineageName',owner=self)
        #Cell.DatatypeProperty('name',owner=self)
        #Cell.DatatypeProperty('divisionVolume',owner=self)
        #Cell.DatatypeProperty('description',owner=self)
        #Cell.DatatypeProperty('wormbaseID', owner=self)
        #Cell.DatatypeProperty('synonym', owner=self, multiple=True)

        if name:
            self.name(name)

        if lineageName:
            self.lineageName(lineageName)

    def blast(self):
        """
        Return the blast name.

        Example::

            >>> c = Cell(name="ADAL")
            >>> c.blast() # Returns "AB"

        Note that this isn't a Property. It returns the blast extracted from the ''first''
        lineageName saved.
        """
        import re
        try:
            ln = self.lineageName()
            x = re.split("[. ]", ln)
            return x[0]
        except:
            return ""

    def daughterOf(self):
        """ Return the parent(s) of the cell in terms of developmental lineage.

        Example::

            >>> c = Cell(lineageName="AB plapaaaap")
            >>> c.daughterOf() # Returns [Cell(lineageName="AB plapaaaa")]"""
        ln = self.lineageName()
        parent_ln = ln[:-1]
        return Cell(lineageName=parent_ln)

    def parentOf(self):
        """ Return the direct daughters of the cell in terms of developmental lineage.

        Example::

            >>> c = Cell(lineageName="AB plapaaaap")
            >>> c.parentOf() # Returns [Cell(lineageName="AB plapaaaapp"),Cell(lineageName="AB plapaaaapa")] """
