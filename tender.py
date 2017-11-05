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
        model.Quotes_Lanes = Param(model.Quotes)
        model.Quotes_Carrier = Param(model.Quotes)
        model.Quotes_Mode = Param(model.Quotes)
        model.Quotes_Price = Param(model.Quotes)

            #Lanes
        model.Lanes_Nodes = Param(model.Lanes)
        model.Lanes_Origin = Param(model.Lanes)
        model.Lanes_Destination = Param(model.Lanes)
        model.Lanes_Product = Param(model.Lanes)
        model.Lanes_Carrier = Param(model.Lanes)

            #Tendering
        model.Carrier_current = Param(model.Lanes,model.Carriers, within = Binary)

        #Variables
        model.VOL = Var(model.Lanes_Modes_Carriers_Products)
        model.UNMET_VOL = Var(model.Lanes_Products)
        model.CARRIER_LANE = Var(model.Lanes,model.Carriers)

        #Minimize total costs
        def obj_fxn(model):
            return Null

        def minimumQuantity(model, c, cf):
            if sum(1 for (lane, mode) in model.LM if (l, c, m) in model.LCM if (l, c, m) in model.LCM if
                   model.lFromCountry[l] == cf) > 0:
                return sum(model.ALLOC_MT[l, c, m] for (l, m) in model.LM if (l, c, m) in model.LCM if
                           model.lFromCountry[l] == cf) >= \
                       sum(model.lVolumeMTPerYear[l] for l in model.L if model.lFromCountry[l] == cf) * \
                       model.BIN_CARRIER_CTRYFROM[c, cf] * model.tenderCtryFromMinShare[cf]
            else:
                return Constraint.NoConstraint

        model.csMinShareCtryFrom = Constraint(model.Carriers, model.Carriers_F, rule=minimumQuantity)




    def solve_pyomo_model(self, solver='glpk', settings, debug_mode=False, maxiter=10):
        
        opt = SolverFactory(solver, settings)



        
