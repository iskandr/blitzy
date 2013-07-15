from collections import namedtuple
import numpy as np 

Index = namedtuple('Index', ('iname', 'start', 'stop', 'step'))

class Kernel(object):

    def __init__(self, args=None, indices=None, stmts=None):
      if args is None: args = {}
      if indices is None: indices = {}
      if stmts is None: stmts = set([])

      # mapping from names to values
      self.args = dict(args)

      # mapping from name of data argument to 
      self.indices = dict(indices)
      
      # set of stmts as string literals 
      self.stmts = stmts

    def combine(self, other):
      args = {}
      args.update(self.args)
      args.update(other.args)

      indices = {}
      indices.update(self.indices)
      indices.update(other.indices)

      stmts = set([])
      stmts.update(self.stmts)
      stmts.update(other.stmts)
      return Kernel(args, indices, stmts)
                       


class Expr(object):
    def __init__(self, my_kernel=None):
        if my_kernel is None:
          my_kernel = Kernel({}, {}, set([]))

        self.my_kernel = my_kernel

    

class Each(Expr):
  _name_counter = 0

  def __init__(self, xs, name = None, axis = None):

    self.kernel = Kernel()
    assert isinstance(xs, np.ndarray)
    self.arg = xs 

    if name is None:
        self._name_counter += 1
        name = "arg%d" % self._name_counter

    self.axis = axis 

  

 

