import PyOpenWorm as P
from PyOpenWorm import *

__all__ = ['Connection']

class SynapseType:
    Chemical = 'send'
    GapJunction = 'gapJunction'

class Termination:
    Neuron = 'neuron'
    Muscle = 'muscle'

class Connection():
    """Connection between Cells

    Parameters
    ----------
    pre_cell : string, Muscle or Neuron, optional
        The pre-synaptic cell
    post_cell : string, Muscle or Neuron, optional
        The post-synaptic cell
    number : int, optional
        The weight of the connection
    syntype : {'gapJunction', 'send'}, optional
        The kind of synaptic connection. 'gapJunction' indicates
        a gap junction and 'send' a chemical synapse
    synclass : string, optional
        The kind of Neurotransmitter (if any) sent between `pre_cell` and `post_cell`

    Attributes
    ----------
    termination : {'neuron', 'muscle'}
        Where the connection terminates. Inferred from type of post_cell
    """
    def __init__(self,
                 pre_cell=None,
                 post_cell=None,
                 number=None,
                 syntype=None,
                 synclass=None,
                 termination=None,
                 **kwargs):


class Connection():
    """A representation of the connection between neurons. Either a gap junction
    or a chemical synapse

    TODO: Add neurotransmitter type.
    TODO: Add connection strength
    """

    multiple=True
    def __init__(self,**kwargs):
        P.Property.__init__(self,'connection',**kwargs)
        self._conns = []

    def get(self,pre_post_or_either='pre',**kwargs):
        """Get a list of connections associated with the owning neuron.

           Parameters
           ----------
           type: What kind of junction to look for.
                        0=all, 1=gap junctions only, 2=all chemical synapses
                        3=incoming chemical synapses, 4=outgoing chemical synapses
           Returns
           -------
           list of Connection
        """
        c = []
        if pre_post_or_either == 'pre':
            c.append(P.Connection(pre_cell=self.owner,**kwargs))
        elif pre_post_or_either == 'post':
            c.append(P.Connection(post_cell=self.owner,**kwargs))
        elif pre_post_or_either == 'either':
            c.append(P.Connection(pre_cell=self.owner,**kwargs))
            c.append(P.Connection(post_cell=self.owner,**kwargs))
        for x in c:
            for r in x.load():
                yield r

    def count(self,pre_post_or_either='pre',syntype=None, *args,**kwargs):
        """Get a list of connections associated with the owning neuron.

           Parameters
           ----------
           See parameters for PyOpenWorm.connection.Connection

           Returns
           -------
           int
               The number of connections matching the paramters given
        """
        options = dict()
        options["pre"] = """
                     ?x c:pre_cell ?z .
                     ?z sp:value <%s> .
                     """ % self.owner.identifier()
        options["post"] = """
                      ?x c:post_cell ?z .
                      ?z sp:value <%s> .
                      """ % self.owner.identifier()
        options["either"] = " { %s } UNION { %s } . " % (options['post'], options['pre'])

        if syntype is not None:
            if syntype.lower() == 'gapjunction':
                syntype='gapJunction'
            syntype_pattern = "FILTER( EXISTS { ?x c:syntype ?v . ?v sp:value \"%s\" . }) ." % syntype
        else:
            syntype_pattern = ''

        q = """
        prefix ow: <http://openworm.org/entities/>
        prefix c: <http://openworm.org/entities/Connection/>
        prefix sp: <http://openworm.org/entities/SimpleProperty/>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT (COUNT(?x) as ?count) WHERE {
         %s
         %s
        }
        """ % (options[pre_post_or_either], syntype_pattern)

        res = 0
        for x in self.conf['rdf.graph'].query(q):
            res = x['count']
        return int(res)

    def set(self, conn, **kwargs):
        """Add a connection associated with the owner Neuron

           Parameters
           ----------
           conn : PyOpenWorm.connection.Connection
               connection associated with the owner neuron

           Returns
           -------
           A PyOpenWorm.neuron.Connection
        """
        #XXX: Should this create a Connection here instead?
        assert(isinstance(conn, P.Connection))
        self._conns.append(conn)
