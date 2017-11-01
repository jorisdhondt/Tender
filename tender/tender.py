from pyomo.environ import *
from pyomo.opt import TerminationCondition
from pyomo.opt import SolverFactory
import numpy as np
import pandas as pd

class Tender():

    def __init__(self, inputData):
        df = pd.read_csv(inputData)
        #extract Lanes, Nodes, Quotes & Carriers
        self.df = df


    def create_pyomo_model(self, debug_mode=False):

        print('Creating Pyomo Model (debug=%s)' % debug_mode)

        model = ConcreteModel()

        #Sets
        model.Lanes = Set(initialize=self.lanes)
        model.Nodes = Set(initialize=self.nodes)
        model.Quotes = Set(initialize=self.quotes)
        model.Carriers = Set(initialize=self.carriers)
        model.Modes = Set(initialize=self.modes)
        model.Products = Set(initialize = self.products)

        #Parameteers
            #Quotes


            #Lanes
        model.Lanes_Nodes = Param(model.Lanes)
        model.Lanes_Product = Param(model.Lanes)
        model.Lanes_Carrier = Param(model.Lanes)

        #Variables
        model.VOL = Var(model.Lanes_Modes_Carriers_Products)
        model.UNMET_VOL = Var(model.Lanes_Products)

        #Minimize total costs
        def obj_fxn(model):
            return Null

    def solve_pyomo_model(self, solver='glpk', debug_mode=False, maxiter=10):
        
        opt = SolverFactory(solver)

        
