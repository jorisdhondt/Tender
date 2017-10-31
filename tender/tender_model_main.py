import sys
print(sys.path)

import pyodbc

from coopr.pyomo import *
from tender_model import model
from pyomo.opt import SolverFactory, SolverStatus, TerminationCondition
from collections import defaultdict
from os.path import expanduser
home = expanduser("~")