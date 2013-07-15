from collections import namedtuple
import numpy as np 

IndexRange = namedtuple('IndexRange', ('iname', 'start', 'stop', 'step'))

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
  def __init__(self):
    self.kernel = Kernel()
  
  def sum(self, axis = None):
    return Sum(self, axis = None)

  def mean(self):
    return Mean(self, axis = None)

class Const(Expr):
    def __init__(self, value):
      Expr.__init__(self)
      self.value = value 
  
    def expr_str(self):
      return "%s" % self.value 

def as_expr(x):
  if isinstance(bool, int, long, float):
      return Const(x)
  assert isinstance(x, Expr)
  return x 

class Each(Expr):
  _name_counter = 0

  def __init__(self, x, name = None, axis = None):    
    Expr.__init__(self)
    assert axis is None
    assert isinstance(x, np.ndarray)
    self.x = x
    
    if name is None:
        self._name_counter += 1
        name = "arg%d" % self._name_counter

    self.name = name 
    self.axis = axis 

    assert name not in self.kernel.args, \
            "Already have an argument named" % name
    self.kernel.args[name] = x
    
    iname = "%s_idx" % name 
    irange = IndexRange(iname, 0, len(x), 1)
    self.kernel.indices[name] = irange

  def __str__(self):
      print "Each(%s, name = %s, axis = %s)" % (self.x, self.name, self.axis)


class Add(Expr):
  def __init__(self, x, y):
    self.kernel = Kernel()
    self.kernel.combine(x)
    self.kernel.combine(y)
    self.x = x
    self.y = y
    
  def expr_str(self):
    return "%s + %s" % (x.expr_str(), y.expr_str())


class Sum(Expr):
  pass 

class Mean(Expr):
  pass

 

