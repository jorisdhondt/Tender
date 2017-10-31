from pyomo.environ import *
from pyomo.opt import TerminationCondition
from pyomo.opt import SolverFactory
import numpy as np
import pandas as pd

class Tender():

    def __init__(self, inputData):
        df = pd.read_csv(inputData)

        self.df = df


    def create_pyomo_model(self, debug_mode=False):


        print('Creating Pyomo Model (debug=%s)' % debug_mode)

        model = ConcreteModel()

        model.Lanes = Set(initialize=self.lanes)
        model.Nodes = Set(initialize=self.nodes)

    def solve_pyomo_model(self, solver='glpk', debug_mode=False, maxiter=10):
        
        opt = SolverFactory(solver)

        
